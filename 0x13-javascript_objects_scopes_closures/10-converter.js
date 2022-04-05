#!/usr/bin/node
exports.converter = function (base) {
  function toString (num) {
    return num.toString(base);
  }
  return toString;
};
