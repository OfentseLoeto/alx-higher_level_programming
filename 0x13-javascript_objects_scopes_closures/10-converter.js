#!/usr/bin/node

// function that converts a number from base
// 10 to another base passed as argument

exports.converter = function (base) {
  return function convertToBase (number) {
    if (number === 0) {
      return '';
    } else {
      return convertToBase(number / base | 0) + '0123456789abcdefghijklmnopqrstuvwxyz'[number % base | 0];
    }
  };
};
