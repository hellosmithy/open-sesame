import sublime, sublime_plugin, os

class OpenSesameCommand(sublime_plugin.TextCommand):

	def run(self, edit):
		# Load the plugin settings
		plugin_settings = sublime.load_settings('OpenSesame.sublime-settings')

		# Override the plugin settings project-specific settings if specified
		project_data = sublime.active_window().project_data()
		if project_data and project_data.get('settings') and project_data.get('settings').get('open_sesame'):
			project_settings = project_data.get('settings').get('open_sesame')
			for setting in project_settings:
				plugin_settings.set(setting, project_settings[setting])


		self.layout = plugin_settings.get('layout')
		self.component_paths = plugin_settings.get('paths')

		# Get the current project directory
		window = sublime.active_window()
		project_dir = window.folders()[0]

		# Replace placeholders in component paths
		component_paths = [ component_path.replace('$ProjectDir', project_dir) for component_path in self.component_paths ]

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

		# Bail out if no component was selected
		if index == -1:
			return
		
		# Get the name of the selected component
		selected_component = self.components[index]
		component_name = selected_component['name']
		component_path = selected_component['path']

		# Get the paths to the individual files within the component directory
		js_filename = component_path + '/' + component_name + '.js'
		html_filename = component_path + '/' + component_name + '.html'
		sass_filename = component_path + '/_' + component_name + '.scss'

		# Lay out the window panes
		window = sublime.active_window()
		window.set_layout(self.layout)

		window.focus_group(0)
		window.open_file(html_filename)

		window.focus_group(1)
		window.open_file(sass_filename)

		window.focus_group(2)
		window.open_file(js_filename)

		# Get the views so that we can add close listeners
		html_view = window.active_view_in_group(0)
		sass_view = window.active_view_in_group(1)
		js_view = window.active_view_in_group(2)

		CloseListener.groups.append([html_view, sass_view, js_view])


class CloseListener(sublime_plugin.EventListener):

	groups = []

	def on_close(self, view):
		matchedGroups = [group for group in self.groups if view in group]
		if len(matchedGroups) > 0:
			for matchedGroup in matchedGroups:
				otherViews = [matchedView for matchedView in matchedGroup if matchedView != view]
				self.groups.remove(matchedGroup)
				for otherView in otherViews:
					otherView.close()


