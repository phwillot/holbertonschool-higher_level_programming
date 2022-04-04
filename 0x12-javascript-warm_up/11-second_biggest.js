#!/usr/bin/node
if (process.argv.length <= 3) console.log('0');
else {
  let max = process.argv[2];
  let secondMax = process.argv[2];

  for (const value of process.argv) { if (value > max) max = value; }

  for (const value of process.argv) { if (value < max && secondMax < value) secondMax = value; }

  console.log(secondMax);
}
