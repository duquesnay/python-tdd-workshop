from pytest import skip
from currency_converter import extract_currency, extract_number


def test_return_something():
    assert extract_currency('SGD') is not None


def test_return_SGD_when_SGD():
    assert extract_currency('SGD') == 'SGD'


def test_return_EUR_when_EuroSig():
    assert extract_currency('€') == 'EUR'


def test_return_USD_when_Dollar():
    assert extract_currency('$') == 'USD'


def test_return_HKD_when_HkDollar():
    assert extract_currency('HK$') == 'HKD'


def test_return_VND_when_Dong():
    assert extract_currency('₫') == 'VND'


def test_should_extract_SGD_currency_from_number():
    assert extract_currency('SGD1234.45') == 'SGD'


def test_should_extract_EUR_currency_from_number():
    assert extract_currency('€1234.45') == 'EUR'


def test_should_extract_SGD_currency_with_space_from_number():
    assert extract_currency('SGD 1234.45') == 'SGD'
 

def test_should_extract_EUR_with_space_currency_from_number():
    assert extract_currency('€ 1234.45') == 'EUR'


def test_should_extract_original_if_unknown():
    assert extract_currency('chibjdi123.456') == 'chibjdi'


def test_should_extract_number_with_currency_prefix():
    assert extract_number('SGD123.45') == '123.45'
    assert extract_number('SGD2,200.00') == '2,200.00'


def test_should_extract_number_with_currency_prefix_and_space():
    assert extract_number('SGD 123.45') == '123.45'
    assert extract_number('SGD 2,200.00') == '2,200.00'
