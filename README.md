Sublime-JSLint
==============

Fast and easy JSLint build system for Sublime Text 2 and Node.JS.

   * Does not require Java&trade;.
   * It has jslint built in; only needs Node.JS installed on your system.
   * It can automatically run JSLint whenever you save a file.
   * Fully configurable linting options.
   * Jump to errors using F4 / Shift+F4.
   * Works on Linux, MacOS and Windows.

Prerequisites
-------------
NodeJS must be installed on your system and you must be able to run 'node' from the command line.

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

### Note for Sublime Text 3 Users:
   * Get files from the package archive and unzip to Packages/JSLint directory:
      * Linux: ~/.config/sublime-text-3/Packages/JSLint
      * Mac: ~/Library/Application Support/Sublime Text 3/Packages/JSLint
      * Windows: %APPDATA%/Sublime Text 3/Packages/JSLint

```
cd "%APPDATA%/Sublime Text 3/Packages"
C:> mkdir JSHint
C:> cd JSHint

Unzip the files from the package archive here.
```

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
