#!/usr/bin/node

//  prints a message depending of the number of arguments passed
//  If no arguments are passed to the script, print “No argument"
//  If only one argument is passed to the script, print “Argument found”
//  Otherwise, print “Arguments found”

const argc = process.argv.length;
if (argc === 3) {
  console.log('Argument found');
} else if (argc === 2) {
  console.log('No argument');
} else {
  console.log('Arguments found');
}
