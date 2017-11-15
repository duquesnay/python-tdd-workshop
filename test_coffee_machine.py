import pytest


# ---- the tests ---- #
def test_return_something():
    assert give_coffee_price() is not None


def test_return_0_when_it_works():
    pytest.skip()

# ---- the code ---- #
def give_coffee_price():
    return 1
