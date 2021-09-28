import pytest

from lab1.functions import is_unique


@pytest.mark.parametrize(
    "items, expected",
    (([], True), ([1], True), ([1, 2], True), ([100, 100], False), ([1, 2, 1], False)),
)
def test_is_unique(items, expected):
    assert is_unique(items) == expected
