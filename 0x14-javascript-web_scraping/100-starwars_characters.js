#!/usr/bin/node
const axios = require('axios').default;

axios
  .get(`https://swapi-api.hbtn.io/api/films/${process.argv[2]}/`)
  .then((response) => {
    return response.data;
  })
  .then((film) => {
    for (const character of film.characters) {
      axios.get(character).then((response) => {
        console.log(response.data.name);
      });
    }
  });
