#Open Sesame 0.1

A sublime plugin to open all files for a particular component in multiple views.

*Not suitable for public consumption.*

---

### Installation

	cd ~/Library/Application\ Support/Sublime\ Text\ 3/Packages
	git clone git@github.com:fathomlondon/open-sesame.git


### Usage

Press `⌘+⌥+⇧+O` from anywhere within Sublime Text to open the panel.


### Configuration

#### User-level configuration

- Use the `paths` property to define the paths in which to search for components:

	```
	"paths": [
		"$ProjectDir/src/modules/components",
		"$ProjectDir/src/lib/fathom-library/components"
	]
	```

	Paths specified in the `paths` property can use the `$ProjectDir` magic string to refer to the current project directory.

- Use the `layout` property to define the window layout:

	```
	"layout": {
		"cols": [0.0, 0.5, 1.0],
		"rows": [0.0, 0.33333333333333, 1.0],
		"cells": [
			[0, 0, 1, 1],
			[0, 1, 1, 2],
			[1, 0, 2, 2]
		]
	}
	```

	Layouts must contain 3 cells (corresponding to HTML, CSS and JS respectively) and must be specified in the format expected by the [Window.set_layout()](http://www.sublimetext.com/forum/viewtopic.php?f=6&t=7284) method in the Sublime Text plugin API.

Example `User/OpenSesame.sublime-settings` file:

```json
{
	"paths": [
		"$ProjectDir/src/modules/components",
		"$ProjectDir/src/lib/fathom-library/components"
	],
	"layout": {
		"cols": [0.0, 0.5, 1.0],
		"rows": [0.0, 0.4, 1.0],
		"cells": [
			[0, 0, 1, 1],
			[0, 1, 1, 2],
			[1, 0, 2, 2]
		]
	}
}
```

#### Project-level configuration

Default and user-level settings can be overridden within a project by adding an `open_sesame` key to the `settings` property of your Sublime Text project file.

Example `my-project.sublime-project` file:

```json
{
	"folders": [
		{
			"path": "."
		}
	],
	"settings": {
		"open_sesame": {
			"paths": [
				"$ProjectDir/src/app/components",
				"$ProjectDir/src/lib/fathom-components/components"
			],
			"layout": {
				"cols": [0.0, 0.5, 1.0],
				"rows": [0.0, 0.4, 1.0],
				"cells": [
					[0, 0, 1, 1],
					[0, 1, 1, 2],
					[1, 0, 2, 2]
				]
			}
		}
	}
}
```

---

### TODO

- Close all related files when closing a view
