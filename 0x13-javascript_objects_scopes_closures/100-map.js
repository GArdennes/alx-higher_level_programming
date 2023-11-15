#!/usr/bin/node
// script that imports an array and computes a new array.

const originalList = require('./100-data').list;
const newList = originalList.map((value, index) => value * index);
console.log(originalList);
console.log(newList);
