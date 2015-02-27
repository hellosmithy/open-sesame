#Open Sesame 1.0.0

A sublime plugin to open all files for a particular component in multiple views.

*Not suitable for public consumption.*

---

### Installation

	cd ~/Library/Application\ Support/Sublime\ Text\ 3/Packages
	git clone git@github.com:fathomlondon/open-sesame.git


### Usage

- Create an `.open-sesame` file at the root of your project (as explained [here](#project-config))
- Press `⌘+⌥+⇧+o` from anywhere within Sublime Text to open the panel.


### Configuration

#### Default configuration

OpenSesame ships with the following default configuration:

```json
{
	"paths": [],

	"projectType": "angular",

	"projectTypes": {

		"angular": {
			"files": [
				"*.js",
				"*.html",
				"_*.scss"
			],
			"layout": {
				"cols": [0.0, 0.5, 1.0],
				"rows": [0.0, 0.5, 1.0],
				"cells": [
					[0, 0, 1, 2],
					[1, 0, 2, 1],
					[1, 1, 2, 2]
				]
			}
		},

		"react": {
			"files": [
				"*.jsx",
				"*.styl"
			],
			"layout": {
				"cols": [0.0, 0.5, 1.0],
				"rows": [0.0, 1.0],
				"cells": [
					[0, 0, 1, 1],
					[1, 0, 2, 1]
				]
			}
		}

	}
}
```

**Notes:**

- Layouts must be specified in the format expected by the [Window.set_layout()](http://www.sublimetext.com/forum/viewtopic.php?f=6&t=7284) method in the Sublime Text plugin API. You must defined as many cells as files to open.
- The `paths` are not defined yet as it should be defined per project (as we'll see [further down](#project-config)).
- In the `files` section, `*` is replaced by folder name so if your modules require a prefix for a given type
specify it in the following format - `_*.scss` which becomes `_component.scss` or `index.html` (*remains untouched*) if all modules have a naming scheme.


#### User-level configuration

Following the conventions of any sublime settings file, you can override any settings by creating your own `User/OpenSesame.sublime-settings` file. For example if you wanted to redefine the layouts for the 2 default project types:

```json
{
	"projectTypes": {

		"angular": {
			"files": [
				"*.js",
				"*.html",
				"_*.scss"
			],
			"layout": {
				"cols": [0.0, 0.55, 1.0],
				"rows": [0.0, 0.5, 1.0],
				"cells": [
					[0, 0, 2, 1],
					[0, 1, 1, 2],
					[1, 1, 2, 2]
				]
			}
		},

		"react": {
			"files": [
				"*.jsx",
				"*.styl"
			],
			"layout": {
				"cols": [0.0, 1.0],
				"rows": [0.0, 0.5, 1.0],
				"cells": [
					[0, 0, 1, 1],
					[0, 1, 1, 2]
				]
			}
		}

	}
}
```


#### <a name="project-config"></a>Project-level configuration

- Add an `.open-sesame` file to root of your project folder.
- Define the `paths` where to find the components to list.
- Define the `projectType` to let OpenSesame know what file types to open and which layout to use.

Example `.open-sesame` file:

```json
{
	"paths": [
		"$ProjectDir/src/apps",
		"$ProjectDir/src/views",
		"$ProjectDir/src/components"
	],

	"projectType": "react"
}
```

**Note**: Paths specified in the `paths` property can use the `$ProjectDir` magic string to refer to the current project directory.
