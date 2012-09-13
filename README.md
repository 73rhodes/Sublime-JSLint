Sublime-JSLint
==============

JSLint build system for Sublime Text 2, using jslint for node. Optionally, run JSLint whenever
you save a .js, .css, .sass, .less, or .json file. Adds menu items to run JSLint manually or 
change preferences. Jump to next / previous error using F4 / Shift+F4.

Prerequisites
-------------
You must have NodeJS and the JSLint node module installed:
npm -g install jslint

Installation
------------

### Using Package Control:

   * Press Ctrl+Shift+P to bring up the Command Palette (or use Tools > Command Palette menu)
   * Select Package Control: Install Package
   * Type 'JSLint' to find JSLint (with node) for Sublime Text 2
   * Select 'JSLint (with node) for Sublime Text 2' to install


### Not using Package Control:
   * Save files to the Packages/JSLint directory, then relaunch Sublime:
      * Linux: ~/.config/sublime-text-2/Packages/JSLint
      * Mac: ~/Library/Application Support/Sublime Text 2/Packages/JSLint
      * Windows: %APPDATA%/Sublime Text 2/Packages/JSLint

Usage
-----
Any of the following will work:
   * Select 'JSLint' under Tools > Build System and run Build.
   * Select Tools > JSLint
   * Press ctrl-L
   * Just save a .js file

Settings
--------
   * Edit filename extensions under Preferences > Package Settings > JSLint. Any filename extensions there will be jslinted on save.
