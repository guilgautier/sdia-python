import pytest

from lab1.functions import triangle_shape

triangle_strings = [
    "",
    "x",
    "\n".join([" x ", "xxx",]),
    "\n".join(["  x  ", " xxx ", "xxxxx",]),
    "\n".join(["   x   ", "  xxx  ", " xxxxx ", "xxxxxxx",]),
    "\n".join(["    x    ", "   xxx   ", "  xxxxx  ", " xxxxxxx ", "xxxxxxxxx",]),
    "\n".join(
        [
            "     x     ",
            "    xxx    ",
            "   xxxxx   ",
            "  xxxxxxx  ",
            " xxxxxxxxx ",
            "xxxxxxxxxxx",
        ]
    ),
]


@pytest.mark.parametrize("height, expected", enumerate(triangle_strings))
def test_triangle_shape(height, expected):
    shape = triangle_shape(height)
    assert shape == expected
