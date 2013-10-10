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
* Navigate to **Preferences > Package Settings > JSLint > Settings - User**.
* Edit and paste the following json object into that file.
```js
{
    // an array of options to pass to jslint, e.g.
    // ["--white", "--vars"] or maybe ["--indent", "2", "--node", "false"]
    "options" : [

      // examples using predef flag.
      "--predef", "['angular', 'document', '\\$', '_', 'JQuery', 'FB']"
      // tolerate missing 'use strict' pragma.
      ,"--sloppy"
      // suggest an indent level of two spaces.
      ,"--indent", "2"
      // assume node.js to predefine node globals.
      ,"--node"
      // tolerate unfiltered for in.
      //,"--forin"
      // tolerate dangling _ in identifiers.
      ,"--nomen"
      // tolerate many var statements per function.
      ,"--vars"
      // tolerate ++ and --.
      ,"--plusplus"
      // tolerate Douglas Crockford.
      ,"--stupid"
      ,"--todo"

    ]

    // if true, run jslint on save.
    ,"run_on_save" : true

    // a regex string to determine whether jslint
    // should be run on a file.
    // if a match is found (i.e. re.search(filename_filter, filename)),
    // the file will be linted.
    ,"filename_filter": "(\\.js|\\.json)$"


    // jslint command you want to run as an array of strings.
    // E.g.: ["jslint"] or ["/usr/local/bin/jslint"] or ["node", "mylinter.js"]
    // Default is
    //    * Linux: ["node", "~/.config/sublime-text-2/Packages/JSLint/linter.js"]
    //    * Mac: ["node", "~/Library/Application Support/Sublime Text 2/Packages/JSLint/linter.js"]
    //    * Windows: ["node", "%APPDATA%/Sublime Text 2/Packages/JSLint/linter.js"]

    // ,"jslint" : ["jslint"]


    // if your own personal choice of jslint has an output
    // different from the standard which comes with this package,
    // you may have to change line_regex and file_regex
    // check http://docs.sublimetext.info/en/latest/reference/build_systems.html
    // to find out how these regular expressions work. The defaults are:

    // ,"line_regex" : ".*// Line ([0-9]*), Pos ([0-9]*)$"
    // ,"file_regex" : "(^[^# ]+.*$)"
}
```

Troubleshooting
---------------

### "No such file or directory" when saving

When, on saving a .js file, you get this:

    [Errno 2] No such file or directory
    [cmd:  [u'node', ...]]


then probably the command to run nodejs is different on your system.
Navigate to **Preferences > Package Settings > JSLint > Settings - User** to change it.
Add e.g.
```js
{
   "jslint": ["nodejs", "~/.config/sublime-text-2/Packages/JSLint/linter.js"]
}
```
if your node command is `nodejs`.
