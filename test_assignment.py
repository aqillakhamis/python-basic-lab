from assignment import add_numbers, multiply_numbers

def test_add():
    assert add_numbers(2, 3) == 5
    assert add_numbers(-1, 1) == 0

def test_multiply():
    assert multiply_numbers(3, 4) == 12
    assert multiply_numbers(10, 0) == 0
