#!/usr/bin/node
// script that returns the number of occurrences in a list

const occurrenceByUserId = require('./101-data').dict;
const userIdByOccurrence = {};

for (const userId in occurrenceByUserId) {
  const occurrence = occurrenceByUserId[userId];

  if (userIdByOccurrence[occurrence] === undefined) {
    userIdByOccurrence[occurrence] = [];
  }
  userIdByOccurrence[occurrence].push(userId);
}

console.log(userIdByOccurrence);
