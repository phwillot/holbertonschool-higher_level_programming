#!/usr/bin/node
const axios = require('axios').default;
const fs = require('fs');

axios.get(process.argv[2]).then((response) => {
  fs.writeFile(process.argv[3], response.data, (err) => {
    if (err) {
      console.error(err);
    }
  });
});
