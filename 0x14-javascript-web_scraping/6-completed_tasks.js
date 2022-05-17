#!/usr/bin/node
const axios = require('axios').default;

axios.get(process.argv[2]).then((response) => {
  const object = {};
  for (const task of response.data) {
    if (task.completed) {
      if (task.userId in object) {
        object[task.userId]++;
      } else {
        object[task.userId] = 1;
      }
    }
  }
  console.log(object);
});
