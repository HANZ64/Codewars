test.assert_equals(even_or_odd(2), "Even", 'even_or_odd(2)')
test.assert_equals(even_or_odd(1), "Odd", 'even_or_odd(1)')
test.expect(even_or_odd(0) == "Even")
test.expect(even_or_odd(1545452) == "Even")
test.expect(even_or_odd(7) == "Odd")
test.expect(even_or_odd(78) == "Even")
test.expect(even_or_odd(17) == "Odd")
test.expect(even_or_odd(74156741) == "Odd")
test.expect(even_or_odd(100000) == "Even")
test.expect(even_or_odd(-123) == "Odd")
test.expect(even_or_odd(-456) == "Even")