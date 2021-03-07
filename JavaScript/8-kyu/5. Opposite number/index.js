/*
  Title:
    Opposite number

  Kata Link:
    https://www.codewars.com/kata/opposite-number

  Instructions:
    Very simple, given a number, find its opposite.

    Examples:

    1: -1
    14: -14
    -34: 34

  Problem:
    function opposite(number) {
      //your code here
    }
*/

/*=============================================*/

// My solution:

function opposite(number) {
  return number * -1;
}

/*=============================================*/

// 1. Alternative Solution (refactored):

function opposite(number) {
  return(-number);
}

// 2. Alternative Solution:

const opposite = number => -number;

// 3. Alternative Solution:

function opposite(n) {
  return n-n*2;
}

// 4. Alternative Solution:

function opposite(number) {
  return number/-1;
}

/*=============================================*/