#!/usr/bin/node

// script that computes and prints a factorial
// The first argument is integer (argument can be cast as integer)
// used for computing the factorial
// Factorial of NaN is 1
// You must do it recursively
// You must use a function

//function factorial (n) {
  //if (isNaN(n)) {
    //return 1;
//  } else if (n === 0 || n === 1) {
  //  return 1;
 // } else {
   // return n * factorial(n - 1);
  //}
//}
//const n = parseInt(process.argv[2]);
//console.log(`The factorial of ${n} is ${factorial(n)}.`);

function factorial (a) {
  if (a <= 0) {
    return 0;
  } else if (a === 1) {
    return 1;
  } else {
    return (a * factorial(a - 1));
  }
}

const myInt = parseInt(process.argv[2]);
if (isNaN(myInt)) {
  console.log('1');
} else {
  console.log(factorial(myInt));
}

