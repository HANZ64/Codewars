/*
  Title:
    Grasshopper - Summation

  Kata Link:
    https://www.codewars.com/kata/grasshopper-summation

  Instructions:
    Summation

    Write a program that finds the summation of every number from 1 to num. The number will always be a positive integer greater than 0.

    For example:

    summation(2) -> 3
    1 + 2

    summation(8) -> 36
    1 + 2 + 3 + 4 + 5 + 6 + 7 + 8

  Problem:
    var summation = function (num) {
      // Code here
    }
*/

/*=============================================*/

// My solution:

const summation = num => {
  sum = 0
  for (let i = 0; i <= num; i++) {
    sum += i;
  }
  return sum
}

/*=============================================*/

// 1. Alternative Solution:

const summation = n => n * (n + 1) / 2;

// 2. Alternative Solution:

function summation(num) {
  return num * (num + 1) / 2
}

// 3. Alternative Solution (ternary):

var summation = function f(num) {
  return num ? num + f(num-1) : 0;
}

// 4. Alternative Solution:

const summation = num => (
  Array(num).fill(true)
    .reduce((sum, item, index) => sum + index + 1, 0)
);

// 5. Alternative Solution:

var summation = function (num) {
  let i = 1, s=1;
  while(i++<num) {s+=i}
  return s
}

/*=============================================*/