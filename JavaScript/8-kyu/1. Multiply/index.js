/*
  Title:
    Multiply

  Kata Link:
    https://www.codewars.com/kata/multiply

  Instructions:
    This code does not execute properly. Try to figure out why.

  Problem:
    function multiply(a, b){
      a * b
    }
*/

/*=============================================*/

// My solution:

function multiply(a, b) {
  return a * b;
}

/*=============================================*/

// 1. Alternative Solution:

multiply = function (a, b) {
  return a * b;
}

// 2. Alternative Solution:

multiply = (a, b) => a * b;

// 3. Alternative Solution:

const multiply = (a, b) => a * b;

// 4. Alternative Solution:

function multiply(a, b){
  var prod = a * b;
  return prod;
}

// 5. Alternative Solution:

function multiply(a, b){
  if(isNaN(a,b)) {
    return 'Please insert two numbers!';
  }
  return a * b;
}

/*=============================================*/