from unittest.mock import patch

from print_random_number import get_a_random_number_well_formatted


@patch('print_random_number.random')
def test_get_a_random_number_well_formatted(mocked_random):

    mocked_random.return_value = 0.1234
    msg = get_a_random_number_well_formatted()

    assert msg == 'El número exacto es 0.1234!!!'
