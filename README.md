Sublime-JSLint
==============

JSLint build system for Sublime Text 2, using node. 

   * Optionally run JSLint when you save a .js, .css, .sass, .less, or .json file.
   * Menu items to run JSLint manually and set preferences.
   * Jump to error using F4 / Shift+F4.
   * Built-in jslint; only needs Node.JS installed on your system.
   * Runs on Linux, MacOS and Windows.

Prerequisites
-------------
You must have NodeJS installed on your system and be able to run 'node' from the command line.

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
