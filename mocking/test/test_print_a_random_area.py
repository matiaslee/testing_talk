import pytest
from unittest.mock import MagicMock, patch


from print_a_random_area import get_the_area_of_a_random_square


@patch('print_a_random_area.Square')
def test_get_the_area_of_a_random_square(mocked_class_Square):
    mocked_square = MagicMock()
    mocked_square.area.return_value = 9

    mocked_class_Square.return_value = mocked_square

    msg = get_the_area_of_a_random_square()
    expected_msg = 'I am a square with area 9'

    assert msg == expected_msg
