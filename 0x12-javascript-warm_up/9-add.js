#!/usr/bin/code
// script that prints the addition of 2 integers

const myFirst = parseInt(process.argv[2]);
const mySecond = parseInt(process.argv[3]);

function add (a, b) {
  return (a + b);
}

const total = add(myFirst, mySecond);
console.log(total);
