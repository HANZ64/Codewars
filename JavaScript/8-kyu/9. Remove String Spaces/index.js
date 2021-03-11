/*
  Title:
    Remove String Spaces

  Kata Link:
    https://www.codewars.com/kata/remove-string-spaces

  Instructions:
    Simple, remove the spaces from the string, then return the resultant string.

  Problem:
    function noSpace(x){

    }
*/

/*=============================================*/

// My solution:

function noSpace(x) {
  return x.replace(/ /g, '');
}

/*=============================================*/

// 1. Alternative Solution (refactored):

const noSpace = x => x.replace(/ /g, "");

// 2. Alternative Solution:

function noSpace(x){
  return x.replace(/\s/g, '');
}

// 3. Alternative Solution:

function noSpace(x){
  return x.split(' ').join('');
}

// 4. Alternative Solution:

function noSpace(x){
  return x.split(' ').join('').trim();
}

// 5. Alternative Solution:

function noSpace(x){
  if (typeof x === 'string') return x.replace(/ +/g, '');
  console.log(arguments.callee.name + ': Argument must be string!');
}

// 6. Alternative Solution:

function noSpace(x){
  var result = ""
  for(var index = 0; index < x.length; index++){
    if(x[index] !== " "){
      result += x[index];
    }
  }
  return result;
}

/*=============================================*/