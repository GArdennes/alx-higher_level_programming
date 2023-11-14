#!/usr/bin/node
// function that returns the reversed version of a list withouth reverse

exports.esrever = function (list) {
  const reverseList = [];
  for (let i = 0; i < list.length; i++) {
    reverseList.unshift(list[i]);
  }
  return reverseList;
};
