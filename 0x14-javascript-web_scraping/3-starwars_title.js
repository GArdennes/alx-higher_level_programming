#!/usr/bin/node
/* Displays the status code of a GET request */

const request = require('request-promise');
const id = process.argv[2];
const apiUrl = 'https://swapi-api.hbtn.io/api/films/';

request(apiUrl + id + '/')
  .then(response => {
    console.log(JSON.parse(response).title);
  })
  .catch(err => {
    console.error(err);
  });
