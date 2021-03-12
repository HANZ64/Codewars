/*
  Title:
    Even or Odd

  Kata Link:
    https://www.codewars.com/kata/even-or-odd

  Instructions:
    Create a function (or write a script in Shell) that takes an integer as an argument and returns "Even" for even numbers or "Odd" for odd numbers.

  Problem:
    function even_or_odd(number) {
      // ...
    }
*/

/*=============================================*/

// My solution:

function even_or_odd(number) {
  if (number % 2 === 0) {
    return "Even";
  }
  return "Odd";
}

/*=============================================*/

// 1. Alternative Solution (ternary):

function even_or_odd(number) {
  return number % 2 ? "Odd" : "Even"
}

// 2. Alternative Solution:

const even_or_odd = number => number % 2 === 0 ? 'Even' : 'Odd';

// 3. Alternative Solution:

const even_or_odd = n => (n % 2) ? 'Odd' : 'Even';

// 4. Alternative Solution:

const even_or_odd = n => ["Even","Odd"][n&1] ;

/*=============================================*/