#!/usr/bin/node
const axios = require('axios').default;

axios
  .get(`https://swapi-api.hbtn.io/api/films/${process.argv[2]}`)
  .then((response) => {
    console.log(response.data.title);
  });
