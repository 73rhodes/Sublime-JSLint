var jslint = require('./jslint');
var fs = require('fs');

// Skip first two args (node & linter.js)
var args = process.argv;
args.splice(0, 2);

var argsWithVals = ["indent", "maxerr", "maxlen", "predef"];
var valueExpected = null;
var srcFile = null;
var options = {};

args.forEach(function (val, index) {
    if (/^--[^\s]*$/.test(val)) {
        var arg = val.replace(/^--/, '');
        if (argsWithVals.indexOf(arg) >= 0) {
            valueExpected = arg;
        } else {
            //console.log('Setting ' + arg + '=true ')
            valueExpected = null;
            options[arg] = true;
        }
    } else {
        if (valueExpected) {
            if (val.indexOf('[') === 0) {
                val = eval(val);
            }
            //console.log('Setting ' + valueExpected + "=" + val);
            options[valueExpected] = val;
            valueExpected = null;
        } else if (index === args.length - 1) {
            srcFile = val;
        }
    }
});

fs.readFile(srcFile, function (err, data) {
    'use strict';
    if (err) {
        console.log(err);
    } else {
        data = data.toString('utf8');
        data = data.replace(/^\#\!.*/, "");
        var result = jslint(data, options);
        //var len = result.warnings.length;
        var fileMessage = "\n" + srcFile;
        var pad, line, e, sourceLine;
        if (options.json) {
            console.log(JSON.stringify([srcFile, result.warnings]));
        } else {
            console.log(fileMessage);
            result.warnings.forEach(function (val, index) {
                pad = "#" + String(index + 1);
                while (pad.length < 3) {
                    pad = ' ' + pad;
                }
                e = val;
                if (e) {
                    line = ' // Line ' + (e.line + 1) + ', Pos ' + (e.column + 1);
                    console.log(pad + ' ' + e.message);
                    sourceLine = result.lines[e.line] || '';
                    console.log('    ' + sourceLine.replace(/^\s+|\s+$/, "") + line);
                }
            });
        }
    }
});
