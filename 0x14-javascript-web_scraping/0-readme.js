#!/usr/bin/node
/* Reads and prints the contents of a file synchronously */

const fs = require('fs');
const filename = process.argv[2];

try {
  const data = fs.readFileSync(filename, 'utf8');
  console.log(data);
} catch (err) {
  console.error(err);
}
