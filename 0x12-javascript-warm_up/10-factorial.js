#!/usr/bin/node
// script that computes and prints a factorial

const myVar = parseInt(process.argv[2]);

function factorial (arg) {
  if (isNaN(arg)) {
    return (1);
  } else if (arg <= 1) {
    return (1);
  } else {
    return (factorial(arg - 1) * arg);
  }
}
const factor = factorial(myVar);
console.log(factor);
