/*
  Title:
    String repeat

  Kata Link:
    https://www.codewars.com/kata/string-repeat

  Instructions:
    Write a function called repeatString which repeats the given String src exactly count times.

    repeatStr(6, "I") // "IIIIII"
    repeatStr(5, "Hello") // "HelloHelloHelloHelloHello"

  Problem:
    function repeatStr (n, s) {
      return '';
    }
*/

/*=============================================*/

// My solution:

function repeatStr (n, s) {
  return s.repeat(n);
}

/*=============================================*/

// 1. Alternative Solution:

repeatStr = (n, s) => s.repeat(n)

// 2. Alternative Solution:

function repeatStr (n, s) {
  var str="";
  for(var i=0; i < n; i++)
    str+=s;
    return str;
}

// 3. Alternative Solution:

function repeatStr (n, s) {
  var myString = '';
  while(n > 0) {
    myString += s;
    n--;
  }
  return myString;
}

// 4. Alternative Solution:

function repeatStr (n, s) {
  return n > 1 ? s + repeatStr(--n, s) : s;
}

// 5. Alternative Solution:

function repeatStr (n, s) {
  return Array(n+1).join(s);
}

/*=============================================*/