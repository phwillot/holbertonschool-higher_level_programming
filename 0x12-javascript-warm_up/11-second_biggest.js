#!/usr/bin/node
if (process.argv.length > 3) {
  const intArray = process.argv.slice(2).map(Number);
  intArray.sort();
  intArray.pop();
  console.log(intArray.slice(-1)[0]);
} else console.log(0);
