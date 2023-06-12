#!/usr/bin/node

//  prints x times “C is fun”

const arg = process.argv.slice(2);
const x = parseInt(arg);

if (!isNaN(x)) {
  for (let i = 0; i < x; i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrence');
}
