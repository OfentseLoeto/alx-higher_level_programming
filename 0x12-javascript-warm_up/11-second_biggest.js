#!/usr/bin/node

// script that searches the second biggest integer in the list of arguments
// assume all arguments can be converted to integer
// If no argument passed, print 0
// If the number of arguments is 1, print 0

const args = process.argv.slice(2);

if (args.length === 0) {
  console.log(0);
} else if (args.length === 1) {
  console.log(0);
} else {
  const numbers = args.map(num => parseInt(num));
  const sortedNumbers = numbers.sort((a, b) => b - a);
  console.log(sortedNumbers[1]);
}
