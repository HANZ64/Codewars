Test.describe("Basic tests")
Test.assert_equals(no_space('8 j 8   mBliB8g  imjB8B8  jl  B'), '8j8mBliB8gimjB8B8jlB')
Test.assert_equals(no_space('8 8 Bi fk8h B 8 BB8B B B  B888 c hl8 BhB fd'), '88Bifk8hB8BB8BBBB888chl8BhBfd')
Test.assert_equals(no_space('8aaaaa dddd r     '), '8aaaaaddddr')
Test.assert_equals(no_space('jfBm  gk lf8hg  88lbe8 '), 'jfBmgklf8hg88lbe8') 
Test.assert_equals(no_space('8j aam'), '8jaam')

Test.describe("Random tests")
from random import randint
sol=lambda s: s.replace(" ","")
base="abcdefghijklmnoPqrstuvwxyz0123456789      "

for _ in range(40):
    s="".join([base[randint(0,len(base)-1)] for q in range(1,35)])
    Test.it("Testing for "+repr(s))
    Test.assert_equals(no_space(s),sol(s),"It should work for random inputs too")