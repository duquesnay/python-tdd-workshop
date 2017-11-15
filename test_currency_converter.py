import pytest


# ---- the tests ---- #
def test_return_something():
    assert extract_currency('SGD') is not None


def test_return_SGD_when_SGD():
    assert extract_currency('SGD') == 'SGD'


# ---- the code ---- #
def extract_currency(input):
    return None
