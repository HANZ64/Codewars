Test.describe("Basic Tests")
Test.assert_equals(remove_char('eloquent'), 'loquen')
Test.assert_equals(remove_char('country'), 'ountr')
Test.assert_equals(remove_char('person'), 'erso')
Test.assert_equals(remove_char('place'), 'lac')
Test.assert_equals(remove_char('ok'), '')
Test.assert_equals(remove_char('ooopsss'), 'oopss')

Test.describe("Random Tests")
from random import randint
sol=lambda s: s[1:-1]
l="abc"

for _ in range(40):
    s="".join([l[randint(0,len(l)-1)] for x in range(randint(2,20))])
    Test.it("Testing for %s" %s)
    Test.assert_equals(remove_char(s),sol(s),"It should work for random inputs too")