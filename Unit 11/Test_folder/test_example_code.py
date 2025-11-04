import pytest
from example_code import divide


def test_divide_with_correct_input():
    # positive test cases
    assert divide(10, 2) == 5
    assert divide(6, 3) == 2
    assert divide(100, 25) == 4