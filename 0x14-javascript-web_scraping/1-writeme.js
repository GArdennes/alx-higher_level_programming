#!/usr/bin/node
/* Writes a string to a file */

const fs = require('fs');
const filename = process.argv[2];
const text = process.argv[3];

try {
  fs.writeFileSync(filename, text, 'utf8');
} catch (err) {
  console.error(err);
}
