import re

CURRENCY_DICT = {
            '€': 'EUR',
            'HK$': 'HKD',
            '$': 'USD',
            '₫': 'VND'
            }


def extract_currency(input):
    if input is None:
        return None
    prefix = extract_prefix(input)
    return CURRENCY_DICT.get(prefix, prefix)


def extract_prefix(input):
    return input.rstrip('1234567890,. ')
    
    
def extract_number(input):
    if input is None: 
        return None
    return re.search(r'(\d|\.|,)+', input).group(0)
    