import pytest


def addition(x, y):
    return x + y


def test_simple_addition():
    result = addition(1, 1)
    expected_result = 2
    assert result == expected_result


@pytest.mark.parametrize(
    "x, y, expected",
    [
        (0, 0, 0),
        (1, 1, 2),
        (2, 1, 3),
        (3, 2, 5),
        (4, 3, 7),
        (5, 5, 10),
        (6, 8, 14),
    ],
)
def test_multiple_addition(x, y, expected):
    assert addition(x, y) == expected


def test_raise_type_error_when_something_is_called():
    with pytest.raises(TypeError):
        # call_something_that_raises_TypeError()
        raise TypeError()
