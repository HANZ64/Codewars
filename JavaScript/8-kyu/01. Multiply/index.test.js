Test.assertEquals(multiply(1,1), 1);
Test.assertEquals(multiply(2,1), 2);
Test.assertEquals(multiply(2,2), 4);
Test.assertEquals(multiply(3,5), 15);

Test.describe('Some random tests', function() {
  for(let i=0; i<100; i++) {
    let [a,b] = [r()*100|0, r()*100|0];
    Test.assertEquals(multiply(a,b), a*b);
  }
})