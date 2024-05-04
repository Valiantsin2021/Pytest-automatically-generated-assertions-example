import re
import random
import pytest


def generate_password():
    symbols = "!@#$%^&*()?"
    numbers = "0123456789"
    capitals = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    minors = "abcdefghijklmnopqrstuvwxyz"
    password = ""
    length = 8
    for i in range(length):
        password += symbols[random.randint(0, len(symbols) - 1)]
        password += numbers[random.randint(0, len(numbers) - 1)]
        password += capitals[random.randint(0, len(capitals) - 1)]
        password += minors[random.randint(0, len(minors) - 1)]
    return password


@pytest.mark.parametrize(
    "test_input,expected",
    [
        (generate_password(), "[a-z]"),
        (generate_password(), "[A-Z]"),
        (generate_password(), "[0-9]"),
        (generate_password(), "[!@#$%^&*()]"),
    ],
)
def test_generate_password(test_input, expected):
    assert len(test_input) == 32
    assert re.search(expected, test_input)

if __name__ == "__main__":
    pytest.main([__file__])
