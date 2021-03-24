var array1 = [true,  true,  true,  false,
              true,  true,  true,  true ,
              true,  false, true,  false,
              true,  false, false, true ,
              true,  true,  true,  true ,
              false, false, true,  true ];
            
var array2 = [];
for (var index = 0; index < 500; index++)
  array2.push(true);
for (var index = 0; index < 5; index++)
  array2.push(undefined);
for (var index = 0; index < 100; index++)
  array2.push(false);
              
var array3 = [];
for (var index = 0; index < 500; index++)
  array3.push(null);
for (var index = 0; index < 5; index++)
  array3.push(undefined);
for (var index = 0; index < 100; index++)
  array3.push(false);
  
Test.expect(countSheeps(array1) == 17, "There are 17 sheeps in total, not " + countSheeps(array1))
Test.expect(countSheeps(array2) == 500, "There are 500 sheeps in total, not " + countSheeps(array2))
Test.expect(countSheeps(array3) == 0, "There are no sheeps at all, you counted " + countSheeps(array3))