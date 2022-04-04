#!/usr/bin/node
const parsed = parseInt(process.argv[2]);
if (isNaN(parsed)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < parsed; i++) {
    console.log('C is fun');
  }
}
