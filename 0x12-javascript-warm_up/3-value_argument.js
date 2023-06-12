#!/usr/bin/node

/*
 * Script that print the argument passed to it
 */

const [arg] = process.argv.slice(2);

if (arg === undefined) {
  console.log('No argument');
} else {
  console.log(arg);
}
