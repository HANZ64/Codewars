/*
  Title:
    Counting sheep...

  Kata Link:
    https://www.codewars.com/kata/counting-sheep-dot-dot-dot

  Instructions:
    Consider an array/list of sheep where some sheep may be missing from their place. We need a function that counts the number of sheep present in the array (true means present).

    For example,

    [true,  true,  true,  false,
      true,  true,  true,  true ,
      true,  false, true,  false,
      true,  false, false, true ,
      true,  true,  true,  true ,
      false, false, true,  true]

    The correct answer would be 17.

    Hint: Don't forget to check for bad values like null/undefined

  Problem:
    function countSheeps(arrayOfSheep) {
      // TODO May the force be with you
    }
*/

/*=============================================*/

// My solution:

function countSheeps(arrayOfSheep) {
  let count = 0;
  for (let i = 0; i < arrayOfSheep.length; i++) {
    if (arrayOfSheep[i] === true) {
      count += 1;
    }
  }
  return count;
}

/*=============================================*/

// 1. Alternative Solution:

function countSheeps(arrayOfSheeps) {
  return arrayOfSheeps.filter(Boolean).length;
}

// 2. Alternative Solution:

function countSheeps(arrayOfSheep) {
  var num = 0;
  
  for(var i = 0; i < arrayOfSheep.length; i++)
    if(arrayOfSheep[i] == true)
      num++;
      
  return num;
}

// 3. Alternative Solution:

let countSheeps = x => x.filter( s => s ).length;

// 4. Alternative Solution:

const countSheeps = arrayOfSheeps => arrayOfSheeps.filter(s => s).length;

/*=============================================*/