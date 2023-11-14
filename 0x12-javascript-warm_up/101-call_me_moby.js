#!/usr/bin/node
// function that executes x times a function.

exports.multi_c = function (x, theFunction) {
  for (let i = 0; i < x; i++) {
    theFunction();
  }
};
