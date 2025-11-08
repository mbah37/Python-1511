import pytest
from lab_11_mbah37_1 import normal_angle

def test_normal_angle_valid_input():
    # Test cases for valid inputs
    assert normal_angle(100) == 100
    assert normal_angle(460) == 100
    assert normal_angle(820) == 100
    assert normal_angle(-100) == 260
    assert normal_angle(-460) == 260
    assert normal_angle(-820) == 260

def test_normal_angle_invalid_input():
    # Test cases for invalid inputs returning None
    assert normal_angle("abc") == None
    assert normal_angle(None) == None
    assert normal_angle([]) == None
    assert normal_angle({}) == None