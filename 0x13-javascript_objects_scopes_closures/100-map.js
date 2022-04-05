#!/usr/bin/node
const listData = require('./100-data').list;
const mappedList = listData.map((x, i) => x * i);

console.log(listData);
console.log(mappedList);
