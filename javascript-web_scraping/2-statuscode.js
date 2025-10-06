#!/usr/bin/node

const request = require('request');
const args = process.argv.slice(2);

request.get(args[0], (err, res) => {
  if (!err) {
    console.log(`code: ${res.statusCode}`);
  } else {
    console.error(err);
  }
});
