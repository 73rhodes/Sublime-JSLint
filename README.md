Sublime-JSLint
==============

Fast and easy JSLint build system for Sublime Text 2 and Node.JS.

   * Does not require Java&trade;.
   * It has jslint built in; only needs [Node.JS](http://nodejs.org) installed on your system.
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
   * Get files from the [package archive](https://github.com/darrenderidder/Sublime-JSLint/archive/master.zip) and unzip to Packages/JSLint directory:
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
   * Bring up the **Command Palette** (`Command+Shift+P` on OS X, `Control+Shift+P` on Linux/Windows), then type `JSLint`.
   * Click the **Tools > JSLint** menu entry.
   * Press `CTRL+L`.
   * Just save a `.js` file.

Settings
--------
* Navigate to **Preferences > Package Settings > JSLint > Settings - Default**.
* To preserve custom settings:
  * copy default settings to **Preferences > Package Settings > JSLint > Settings - User**
  * modify them to your requirements


Troubleshooting
---------------

### "No such file or directory" when saving

When, on saving a .js file, you get this:

    [Errno 2] No such file or directory
    [cmd:  [u'node', ...]]


the command to run node might not be in your path. 

Mac OS X users, ensure that `/usr/local/bin` is in your `$PATH` environment variable.

Linux users, if your node command is 'nodejs', as is the case when installing from some Linux repos,  
navigate to **Preferences > Package Settings > JSLint > Settings - User** to change it, e.g.
```js
{
   "jslint": ["nodejs", "~/.config/sublime-text-2/Packages/JSLint/linter.js"]
}
```

