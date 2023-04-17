#!/usr/bin/node

/* script that prints two arguments passed to it */

const [arg1, arg2] = process.argv.slice(2);
console.log(`${arg1} is ${arg2}`);
