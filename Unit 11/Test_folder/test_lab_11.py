import pytest
from lab_11_mbah37_1 import normal_angle

def test_normal_angle_valid_input():
    assert normal_angle(100) == 100
    assert normal_angle(460) == 100
    assert normal_angle(820) == 100
    assert normal_angle(-100) == 260
    assert normal_angle(-460) == 260
    assert normal_angle(-820) == 260

with pytest.raises((ValueError, TypeError)):
    normal_angle("abc")
