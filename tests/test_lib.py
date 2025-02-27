import pytest

from python_skeleton.lib import myfactorial
from tests.conftest import test_data


@pytest.mark.parametrize("n,expected", test_data)
def test_myfactorial(n, expected):
    assert myfactorial(n) == expected
