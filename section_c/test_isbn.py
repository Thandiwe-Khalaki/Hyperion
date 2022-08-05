from isbn import check_isbn
import pytest


@pytest.mark.parametrize(
    "test_input,expected",
    [("9780316066525", "Valid"), ("ISBN 978-0-596-52068-7", "Valid")],
)
def test_string_lengh(test_input, expected):
    assert check_isbn(test_input) == expected, "Your ISBN must be correct length"


@pytest.mark.parametrize(
    "test_input,expected", [("0330301824", "Invalid"), ("007462542X", "Invalid")]
)
def test_validity(test_input, expected):
    assert check_isbn(test_input) == expected, "Your ISBN must be correct digits"


@pytest.mark.parametrize(
    "test_input,expected",
    [("3540009787", "9783540009788"), ("0316066524", "9780316066525")],
)
def test_if_string_can_be_converted(test_input, expected):
    assert (
        check_isbn(test_input) == expected
    ), "Your ISBN must be correct and 10 digits long"
