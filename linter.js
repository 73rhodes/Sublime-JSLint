var JSLINT = require('./jslint');
var fs = require('fs');

// Skip first two args (node & linter.js)
var args = process.argv;
args.splice(0, 2);

var argsWithVals  = ["indent", "maxerr", "maxlen"];
var valueExpected = null;
var srcFile = null;
var options = {};

args.forEach(function (val, index, array) {
  if (/^--[^\s]*$/.test(val)) {
    var arg = val.replace(/^--/, '');
    if (argsWithVals.indexOf(arg) >= 0) {
      valueExpected = arg;
    } else {
      valueExpected = null;
      options[arg] = true;
    }
  } else {
    if (valueExpected) {
      options[valueExpected] = val;
      valueExpected = null;
    } else if (index === args.length - 1) {
      srcFile = val;
    }
  }
});

var srcString = fs.readFile(srcFile, function (err, data) {
  if (err) {
    console.log(err);
  } else {
    data = data.toString('utf8');
    data = data.replace(/^\#\!.*/, "");
    var success = JSLINT(data, options),
      len = JSLINT.errors.length,
      fileMessage = "\n" + srcFile,
      pad,
      line,
      e,
      i;
    if (options.json) {
      console.log(JSON.stringify([srcFile, JSLINT.errors]));
    } else {
      console.log(fileMessage);
      for (i = 0; i < len; i += 1) {
        pad = "#" + String(i + 1);
        while (pad.length < 3) {
          pad = ' ' + pad;
        }
        e = JSLINT.errors[i];
        if (e) {
          line = ' // Line ' + e.line + ', Pos ' + e.character;
          console.log(pad + ' ' + e.reason);
          console.log('    ' + (e.evidence || '').replace(/^\s+|\s+$/, "") + line);
        }
      }
    }
  }
});
