#Open Sesame 0.1

A sublime plugin to open all files for a particular component in multiple views.

*Not suitable for public consumption.*

---


###Installation

	cd ~/Library/Application\ Support/Sublime\ Text/ 3/Packages
	git clone git@github.com:fathomlondon/open-sesame.git 
	
###Configuration
Specify the directory where sublime should look for components on line 6 of `OpenSesame.py`

	def run(self, edit):
		self.thedir = 'ADD YOUR COMPONENT DIRECTORY HERE'
		#eg: self.thedir = '/Users/tom/Documents/Project/src/js/components'
		...
		
###Use
	cmd + alt + shift + o
	
###Todo

- [x] Get directory from settings file§
- [x] Search multiple directories
- [x] Alternate layouts
- [ ] Close all related files when closing a view	