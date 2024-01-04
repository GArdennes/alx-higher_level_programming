#!/usr/bin/node
/*  computes the number of tasks completed by user id. */

const request = require('request');
const url = process.argv[2];

request(url, (err, response, body) => {
  if (err) console.log(err);
  else {
	  const resp = {};
	  const json = JSON.parse(body);

	  for (const task of json){
		  if (task.completed){
			  resp[task.userId] = (resp[task.userId] || 0) + 1;
		  }
	  }
	  console.log(resp);
  }
});
