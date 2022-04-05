#!/usr/bin/node
const listData = require('./100-data').list;
const mappedList = listData.map(x => x * listData.indexOf(x));

console.log(listData);
console.log(mappedList);
