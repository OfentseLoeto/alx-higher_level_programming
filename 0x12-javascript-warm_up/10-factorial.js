#!/usr/bin/node

//  script that computes and prints a factorial

function factorial (n) {
  if (isNaN(n)) {
    return 1;
  } else if (n === 0) {
    return 1;
  } else {
    return n * factorial(n - 1);
  }
}

// parsing the command line argument
const arg = parseInt(process.argv[2]);

// Computing factorial and print the results

console.log(factorial(arg));
