import pytest
from pytest import skip


# ---- the tests ---- #
def test_return_something():
    assert extract_currency('SGD') is not None


def test_return_SGD_when_SGD():
    skip()
    assert extract_currency('SGD') == 'SGD'


def test_return_EUR_when_EuroSig():
    skip()
    assert extract_currency('€') == 'EUR'


def test_return_USD_when_Dollar():
    skip()
    assert extract_currency('$') == 'USD'


def test_return_HKD_when_HkDollar():
    skip()
    assert extract_currency('HK$') == 'HKD'


# ---- the code ---- #
def extract_currency(input):
    return ''
