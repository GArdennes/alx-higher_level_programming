#!/usr/bin/node
// class Square that defines a square and inherits from Rectangle of 4-rectangle.js

const SquareBase = require('./5-square');

class Square extends SquareBase {
  charPrint (c) {
    for (let i = 0; i < this.size; i++) {
      let row = '';
      for (let j = 0; j < this.size; j++) {
        if (c === undefined) {
          c = 'X';
        }
        row += c;
      }
      console.log(row);
    }
  }
}

module.exports = Square;
