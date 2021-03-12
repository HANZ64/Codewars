/*
  Title:
    Convert boolean values to strings 'Yes' or 'No'

  Kata Link:
    https://www.codewars.com/kata/convert-boolean-values-to-strings-yes-or-no

  Instructions:
    Complete the method that takes a boolean value and return a "Yes" string for true, or a "No" string for false.

  Problem:
    function boolToWord( bool ){
      //...
    }
*/

/*=============================================*/

// My solution:

function boolToWord(bool) {
  if (bool) {
    return "Yes";
  } else {
    return "No";
  }
}

/*=============================================*/

// 1. Alternative Solution (refactored):

function boolToWord(bool) {
  if (bool) {
    return "Yes";
  }
  return "No";
}

// 2. Alternative Solution (refactored 2):

function boolToWord(bool) {
  if (bool) return 'Yes';
  return 'No';
}

// 3. Alternative Solution (switch case):

function boolToWord( bool ){
  switch (bool) {
    case true: 
      return 'Yes'
    case false: 
      return 'No'    
  }
}

// 4. Alternative Solution (ternary):

function boolToWord( bool ){
  return bool ? 'Yes':'No';
}

// 5. Alternative Solution:

const boolToWord = bool => bool ? 'Yes' : 'No';

// 6. Alternative Solution:

function boolToWord( bool ){
  return ['No','Yes'][+bool];
}

// 7. Alternative Solution:

const boolToWord = (i) => i && 'Yes' || 'No'

// 8. Alternative Solution:

boolToWord=ъ=>Math.random()<0.5?'Yes':'No'

/*=============================================*/