Sublime-JSLint
==============

[JSLint](http://www.jslint.com/) plugin for Sublime Text 2, using [node](http://nodejs.org). 

   * Optionally run JSLint when you save a `.js` or `.json` file.
   * Run JSLint on a folder from side bar context menu.
   * Jump to errors using `F4` / `Shift+F4`.
   * Menu items to run JSLint manually and set preferences.
   * Only needs [NodeJS installed on your system](http://nodejs.org/download/).
   * Runs on Linux, MacOS and Windows.

Prerequisites
-------------
* **Linux, Windows**: You must have NodeJS installed on your system and be able to run `node` from the command line.
* **Mac OS**: Being able to run `node` from the command line is not enough for you guys, since GUI applications may not get the same `PATH` environment that your console has. See [this post](http://serverfault.com/questions/16355/how-to-set-global-path-on-os-x) on serverfault for a way to define the `PATH` env for GUI applications **and** the console; or manually set the filepath to your `node` or `jslint` executable in the [settings](#settings) file.

You can download **node** from the [node download page](http://nodejs.org/download/).

Installation
------------

### Using [Package Control](http://wbond.net/sublime_packages/package_control):
  * Bring up the **Command Palette** (`Command+Shift+P` on OS X, `Control+Shift+P` on Linux/Windows).
  * Select `Package Control: Install Package`.
  * Type `JSLint` to find `JSLint (with node) for Sublime Text 2`.
  * Select `JSLint (with node) for Sublime Text 2` to install.


### Not using Package Control:
   * Save files to the `Packages/JSLint` directory, then relaunch Sublime:
      * Linux: `~/.config/sublime-text-2/Packages/JSLint`
      * Mac: `~/Library/Application Support/Sublime Text 2/Packages/JSLint`
      * Windows: `%APPDATA%/Sublime Text 2/Packages/JSLint`

Usage
-----
Any of the following will work:
   * Bring up the **Command Palette** (`Command+Shift+P` on OS X, `Control+Shift+P` on Linux/Windows), then
      * type `JSLint: File` to run JSLint on the current file or
      * type `JSLint: Containing Folder` to run JSLint on the whole folder containing the current file.
   * Right click a folder inside the **Side Bar** and click **JSLint Folder**.
   * Click the **Tools > JSLint** menu entry.
   * Press `CTRL+ALT+L`.
   * Just save a `.js` file.

Settings
--------
* Navigate to **Preferences > Package Settings > JSLint > Settings - User**.
* Edit and paste the following json object into that file.
```js
{
    // an array of options to pass to jslint, e.g.
    // ["--white", "--vars"] or maybe ["--indent", "2", "--node", "false"]
    // see https://github.com/reid/node-jslint
    // or http://www.jslint.com/lint.html#options.
    "options" : [
        
        // assume node.js to predefine node globals,
        // defaults to true in `node-jslint`.
        "--node", "false"
        
        // ES5 syntax should be allowed,
        // defaults to true in `node-jslint`.
        ,"--es5", "false"
        
        // tolerate missing 'use strict' pragma
        // do not use this pragma unless you know what you are doing.
        // ,"--sloppy"
        
        // suggest an indent level of two spaces.
        // ,"--indent", "2"
        
        // tolerate unfiltered for in.
        // ,"--forin"
        
        // tolerate dangling _ in identifiers.
        // ,"--nomen"
        
        // tolerate many var statements per function.
        // ,"--vars"
        
        // tolerate ++ and --.
        // ,"--plusplus"
        
        // tolerate stupidity.
        // ,"--stupid"

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
    //    * Linux: ["node", "~/.config/sublime-text-2/Packages/JSLint/node_modules/jslint/bin/jslint"]
    //    * Mac: ["node", "~/Library/Application Support/Sublime Text 2/Packages/JSLint/node_modules/jslint/bin/jslint"]
    //    * Windows: ["node", "%APPDATA%/Sublime Text 2/Packages/JSLint/node_modules/jslint/bin/jslint"]
    // using node-jslint v0.1.9. https://github.com/reid/node-jslint/tree/v0.1.9

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

Contributors
------------
   * Darren DeRidder
   * Jan Raasch
