import sublime, sublime_plugin, os, logging, json

class OpenSesameCommand(sublime_plugin.TextCommand):

	def run(self, edit):

		# Get the current project directory
		window = sublime.active_window()
		project_dir = window.folders()[0]

		# Load the plugin settings
		plugin_settings = sublime.load_settings('OpenSesame.sublime-settings')
		self.plugin_settings = plugin_settings

		# Override the plugin settings with project-specific settings if specified
		project_settings = None
		project_settings_file = None
		self.project_data = None

		if os.path.exists(project_dir + '/.open-sesame'):
			project_settings_file = open(project_dir + '/.open-sesame')
			logging.debug('found project settings file .open-sesame')
		else:
			window.show_quick_panel([['OpenSesame Error', 'Missing configuration file in root (.open-sesame file)']], None)

		if project_settings_file:
			self.project_data = json.load(project_settings_file)


		if self.project_data:
			project_settings = self.project_data

		self.component_paths = project_settings.get('paths') if project_settings and project_settings.get('paths') else plugin_settings.get('paths')

		# Replace placeholders in component paths
		component_paths = [ component_path.replace('$ProjectDir', project_dir) for component_path in self.component_paths ]

		# Get subdirectories recursively
		component_paths_copy = list(component_paths)
		component_paths = []
		for component_path in component_paths_copy:
			subpaths = [root for root, dirs, files in os.walk(component_path)]
			component_paths += subpaths

		# Filter out any paths that don't exist
		component_paths = [ component_path for component_path in component_paths if os.path.isdir(component_path) ]

		# Build a list of child component { name, path } dictionaries (this creates a list containing a sublist for each of the component paths)
		components_by_path = [ [ { 'name': filename, 'path': component_path + '/' + filename } for filename in os.listdir(component_path) if os.path.isdir(os.path.join(component_path, filename)) ] for component_path in component_paths ]

		# Flatten the array of child components
		components = [ component for sublist in components_by_path for component in sublist ]

		# Store the array of child components
		self.components = components

		# Get a list of component names to display in the panel menu
		component_names = [ component['name'] for component in components ]

		# Display the component names in a panel menu
		window.show_quick_panel(component_names, self.open_component, sublime.MONOSPACE_FONT)


	def open_component(self, index):

		# Get a reference to the active window
		window = sublime.active_window()

		# Bail out if no component was selected
		if index == -1:
			return

		# Get the name of the selected component
		selected_component = self.components[index]
		component_name = selected_component['name']
		component_path = selected_component['path']

		# Get project type
		project_type_key = self.project_data.get('projectType');
		project_type = self.plugin_settings.get('projectTypes').get(project_type_key);

		if project_type is None:
			sublime.set_timeout(lambda: window.show_quick_panel([['OpenSesame Error', 'Cannot find project type: ' + project_type_key]], None), 10)
			return

		# Get project filetypes and layout
		project_file_types = project_type.get('files')
		project_layout = project_type.get('layout')

		# Get the paths to the individual files within the component directory
		paths = []
		for file_type in project_file_types:
			paths.append(component_path + '/' + file_type.replace('*', component_name))
		logging.debug(paths)

		# Open the component source files and get the corresponding views
		views = [ window.open_file(path) for path in paths ]

		# Lay out the window panes
		window.set_layout(project_layout)

		# Notify the focus listener that an open operation is in progress
		FocusListener.opening = True

		# Move the views to their corresponding panes
		for groupIndex, view in enumerate(views):
			groupViews = window.views_in_group(groupIndex)
			if not view in groupViews:
				otherViews = [ otherView for otherView in groupViews ]
				window.set_view_index(view, groupIndex, len(otherViews))

		# Focus the first view
		window.focus_view(views[0])

		# Notify the focus listener that the open operation has completed
		FocusListener.opening = False

		# Register the views with the focus listener to synchronise view focusing and closing
		FocusListener.groups.append(views)


class FocusListener(sublime_plugin.EventListener):

	groups = []
	opening = False
	closing = False
	focusing = False

	def on_activated(self, view):
		if self.opening: return
		if self.closing: return
		if self.focusing: return
		self.focusing = True

		matchedGroups = [group for group in self.groups if view in group]
		if len(matchedGroups) > 0:
			for matchedGroup in matchedGroups:
				otherViews = [matchedView for matchedView in matchedGroup if matchedView != view]
				for otherView in otherViews:
					otherView.window().focus_view(otherView)
			view.window().focus_view(view)

		self.focusing = False

	def on_pre_close(self, view):
		if self.closing: return
		self.closing = True
		matchedGroups = [group for group in self.groups if view in group]
		if len(matchedGroups) > 0:
			for matchedGroup in matchedGroups:
				if matchedGroup in self.groups:
					self.groups.remove(matchedGroup)
					otherViews = [matchedView for matchedView in matchedGroup if matchedView != view]
					for otherView in otherViews:
						otherView.close()
		self.closing = False
