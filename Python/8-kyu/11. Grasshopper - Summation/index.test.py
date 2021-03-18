@test.describe('Basic tests')
def basic_tssts():
    test.assert_equals(summation(1), 1)
    test.assert_equals(summation(8), 36)
    test.assert_equals(summation(22), 253)
    test.assert_equals(summation(100), 5050)
    test.assert_equals(summation(213), 22791)

@test.describe('Random tests')
def random_tests():
    from random import randint
    
    solution = lambda num: num * (num + 1) / 2
    
    for i in range(100):
        rand = randint(1, 500)
        test.assert_equals(summation(rand), solution(rand))