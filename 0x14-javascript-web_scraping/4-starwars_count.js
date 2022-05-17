#!/usr/bin/node
const axios = require('axios').default;

axios
  .get(process.argv[2])
  .then((response) => {
    let counter = 0;
    const films = response.data.results;
    for (const film of films) {
      const characters = film.characters;
      for (const character of characters) {
        if (character.includes('18')) {
          counter++;
        }
      }
    }
    console.log(counter);
  })
  .catch((err) => {
    console.error(err);
  });
