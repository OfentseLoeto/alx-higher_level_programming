#!/usr/bin/node

// Finding the second largest number in
// an array of integers

function findSecondLargest (args) {
  if (args.length < 2) {
    return 0;
  }

  let largest = Number.MIN_SAFE_INTEGER;
  let secondLargest = Number.MIN_SAFE_INTEGER;

  for (let i = 0; i < args.length; i++) {
    const num = parseInt(args[i]);

    if (num > largest) {
      secondLargest = largest;
      largest = num;
    } else if (num > secondLargest && num !== largest) {
      secondLargest = num;
    }
  }
  return secondLargest;
}

// parsing the command line arguments
const args = process.argv.slice(2);

// Finding the second largest integer and print the results
console.log(findSecondLargest(args));
