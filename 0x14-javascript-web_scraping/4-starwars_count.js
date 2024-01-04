#!/usr/bin/node
/* Display the number of movie the character
Wedge Antilles is present */

const request = require('request');
const apiUrl = process.argv[2];

request(apiUrl, (err, response, body) => {
  if (err) console.log(err);
  else {
    const results = JSON.parse(body).results;
    let count = 0;

    for (const result of results) {
      const characters = result.characters;
      if (characters.some(char => char.search('18') > 0)) {
        count++;
      }
    }
    console.log(count);
  }
});
