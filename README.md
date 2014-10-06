#Open Sesame 0.2.0

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

#### Project-level configuration 0.2.0

Default and user-level settings can be overridden within a project by adding an `.open-sesame` file to root of your project folder

Example `.open-sesame` file:

```
	{
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
		},
		"types": [
			"*.html",
			"*.js",
			"*.styl"
		]
	}
```

Note * is replaced by folder name so if your modules require a prefix for a given type
specify it in the following format - `_*.scss` which becomes `_component.scss` or `index.html` (*remains untouched*) if all modules have a naming scheme. 

