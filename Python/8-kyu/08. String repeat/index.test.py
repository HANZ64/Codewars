test.describe("Basic Tests")
test.assert_equals(repeat_str(4, 'a'), 'aaaa')
test.assert_equals(repeat_str(3, 'hello '), 'hello hello hello ')
test.assert_equals(repeat_str(2, 'abc'), 'abcabc')

test.describe("Random Tests")

_repeat_str = lambda n, s: n * s

import string 
from random import randint, choice

chars = string.ascii_letters + string.digits + string.punctuation + string.whitespace

for _ in range(50):
    word = "".join(choice(chars) for i in range(randint(1, 50)))
    repetition = randint(1, 50)
    test.assert_equals(
        repeat_str(repetition, word),
        _repeat_str(repetition, word)
    )