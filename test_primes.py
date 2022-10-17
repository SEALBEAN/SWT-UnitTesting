import pytest
from contextlib import nullcontext as does_not_raise
from primes import primes
import os


def data():
    # open input
    with open('input.txt', 'r') as f:
        input_str = f.read().split('\n')
        input_test_case = [tuple(map(float, i.split(','))) for i in input_str]

    with open('expected.txt', 'r') as f:
        expected_test_case = f.read().split('\n')

    right_test_case = list(zip(input_test_case, expected_test_case))
    return right_test_case


test_case = data()


@pytest.mark.skipif(1 == 1, reason="tao thich")
def test_primes_with_right_arguments_returns_well_normal_way():
    assert primes(0, 10) == [2, 3, 5, 7]
    assert primes(3, 15) == [3, 5, 7, 11, 13]


@pytest.mark.parametrize(argnames='input, expected', argvalues=test_case)
def test_primes_with_right_arguments_returns_well_parametrize(input, expected):
    left, right = input[0], input[1]
    assert primes(left, right) == expected


# def test_primes_with_right_arguments_returns_well_fixture(data):
# left, right = data[0][0], data[0]

def test_open_datadir(datadir):
    data_path = datadir['a/1-5.txt']

    with open(data_path, 'r') as f:
        data_content = f.read()
    assert data_content == '2, 3, 5'


def test_primes_with_wrong_arguments_returns_well():
    with pytest.raises(TypeError):
        primes('haloo', 'asdasd')

    with pytest.raises(AssertionError):
        primes(1, 10000000)

    with pytest.raises(ValueError):
        primes(1, 2)

    with does_not_raise():
        primes(1, 2)
