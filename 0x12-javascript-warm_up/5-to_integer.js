#!/usr/bin/node
// script that prints two arguments passed to it

const myVar = parseInt(process.argv[2]);
if (isNaN(myVar)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + myVar);
}
