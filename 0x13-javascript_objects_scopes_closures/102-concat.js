#!/usr/bin/node
// script that concats 2 files

const fs = require('fs');
const args = process.argv.slice(2);
const filePath1 = fs.readFileSync('./' + args[0]);
const filePath2 = fs.readFileSync('./' + args[1]);
fs.writeFileSync('./' + args[2], filePath1 + filePath2);
