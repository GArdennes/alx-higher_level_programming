#!/usr/bin/node
// script that searches the second biggest integer

function secondLargest (arg) {
  if (arg.length <= 1) {
    return 0;
  }

  let largest = parseInt(arg[2]);
  let secondLargest = parseInt(arg[2]);

  for (let i = 3; i < arg.length; i++) {
    const currentNumber = parseInt(arg[i]);

    if (currentNumber > largest) {
      secondLargest = largest;
      largest = currentNumber;
    } else if (currentNumber > secondLargest && currentNumber !== largest) {
      secondLargest = currentNumber;
    }
  }

  return secondLargest;
}

console.log((secondLargest(process.argv)));
