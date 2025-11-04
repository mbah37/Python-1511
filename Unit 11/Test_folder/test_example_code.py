import pytest
from example_code import divide


def test_divide_with_correct_input():
    assert divide(10, 2) == 5
    