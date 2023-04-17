#!/usr/bin/node

// script that prints My number: <first argument converted in integer>
//  if the first argument can be converted to an integer:
//  If the argument can’t be converted to an integer, print “Not a number”

const arg = process.argv[2];
const num = parseInt(arg);

if (Number.isNaN(num)) {
  console.log('Not a number');
} else {
  console.log(`My number: ${num}`);
}
