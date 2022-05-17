#!/usr/bin/node
const axios = require('axios').default;

const getCharacters = async () => {
  const film = await axios.get(
    `https://swapi-api.hbtn.io/api/films/${process.argv[2]}/`
  );
  for (const character of film.data.characters) {
    const name = await axios.get(character);
    console.log(name.data.name);
  }
};

getCharacters();
