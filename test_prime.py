from re import I
import pytest
from contextlib import nullcontext as does_not_raise
from prime import primes

# test case
with open('input.txt', 'r') as f:
    file_content = f.readlines()
    input_str = list(map(lambda x: str(x).rstrip('\n'), file_content))
    input_test_case = [tuple(map(float, i.split(','))) for i in input_str]

with open('expected.txt', 'r') as f:
    file_content = f.readlines()
    expected_str = list(map(lambda x: str(x).rstrip('\n'), file_content))
    expected_test_case = [list(map(float, i.split(','))) for i in expected_str]

right_test_case = list(zip(input_test_case, expected_test_case))


def test_primes_with_right_arguments_returns_well_normal_way():
    assert primes(0, 10) == [2, 3, 5, 7]
    assert primes(3, 15) == [3, 5, 7, 11, 13]


@pytest.mark.parametrize(argnames='input, expected', argvalues=right_test_case)
def test_primes_with_right_arguments_returns_well_data_driven(input, expected):
    left, right = input[0], input[1]
    assert primes(left, right) == expected
