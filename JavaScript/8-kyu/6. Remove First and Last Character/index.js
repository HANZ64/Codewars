/*
  Title:
    Remove First and Last Character

  Kata Link:
    https://www.codewars.com/kata/remove-first-and-last-character

  Instructions:
    It's pretty straightforward. Your goal is to create a function that removes the first and last characters of a string. You're given one parameter, the original string. You don't have to worry with strings with less than two characters.

  Problem:
    function removeChar(str){
     //You got this!
    };
*/

/*=============================================*/

// My solution:

function removeChar(str){
  return str.slice(1, -1);
};

/*=============================================*/

// 1. Alternative Solution:

const removeChar = str => str.slice(1,-1)

// 2. Alternative Solution:

function removeChar(str){
 return str.substring(1, str.length-1);
};

// 3. Alternative Solution:

function removeChar(str){
  str1 = str.split('');
  str1.shift();
  str1.pop();
  return str1.join('');
};

/*=============================================*/