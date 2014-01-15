import sublime, sublime_plugin, os

class OpenSesameCommand(sublime_plugin.TextCommand):

	def run(self, edit):
		self.thedir = '/Users/tom/Documents/Tradeweb/tradeweb-uscc/src/js/components'
		self.window = sublime.active_window()
		self.listings = [ name for name in os.listdir(self.thedir) if os.path.isdir(os.path.join(self.thedir, name)) ]
		self.window.show_quick_panel(self.listings, self.open_component, sublime.MONOSPACE_FONT)
		self.settings = sublime.load_settings('OpenSesame.sublime-settings')

	def open_component(self, index):

		if index == -1:
			return

		print('>>>Opening component')
		
		# Generate file paths
		compName = self.listings[index]

		print('>>>Comp name: ' + compName)

		jsFile = self.create_file_ref(compName, 'js')
		htmlFile = self.create_file_ref(compName, 'html')
		sassFile = self.create_file_ref(compName, 'scss')

		layout = {
			"cols": [0.0, 0.5, 1.0],
			"rows": [0.0, 0.5, 1.0],
			"cells": [
				[0, 0, 1, 1],
				[1, 0, 2, 1],
				[0, 1, 2, 2]
			]
		}

		timsLayout = {"cols": [0.0, 0.5, 1.0],"rows": [0.0, 1/3, 1.0],"cells": [[0, 0, 1, 1], [0, 1, 1, 2], [1, 0, 2, 2]]}

		self.window.set_layout(timsLayout)

		self.window.focus_group(0)
		self.window.open_file(htmlFile)

		self.window.focus_group(1)
		self.window.open_file(sassFile)

		self.window.focus_group(2)
		self.window.open_file(jsFile)

	def create_file_ref(self, component, type):
		componentDir = self.thedir + '/' + component + '/'

		print('>>>Creating path for: ' + component + '.' + type)

		if type == 'scss':
			return componentDir + '_' + component + '.' + type
		else:
			return componentDir + component + '.' + type

