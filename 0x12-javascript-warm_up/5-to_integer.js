#!/usr/bin/node
const parsed = parseInt(process.argv[2]);
if (!isNaN(parsed)) {
  console.log('My number:', parsed);
} else {
  console.log('Not a number');
}
