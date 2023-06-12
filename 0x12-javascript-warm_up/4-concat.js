#!/usr/bin/node

// Concatinate two String

const [arg1, arg2] = process.argv.slice(2);

if (arg1 === undefined && arg2 === undefined) {
  console.log('c is undefined');
} else if (arg1 === undefined) {
  console.log('undefined is undefined');
} else {
  console.log(`${arg1 || 'undefined'} is ${arg2 || 'undefined'}`);
}
