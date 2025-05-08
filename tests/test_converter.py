'''
    Test the converter
'''

from main import parse_line


def test_parse_line():
    ''' Test the parse_line function '''
    # test the parse_line function
    assert parse_line('P 2020-01-01 12:00:00 EUR 1.00 USD') == {
        'date': '2020-01-01',
        'time': '12:00:00',
        'commodity': 'EUR',
        'amount': '1.00',
        'currency': 'USD'
    }

def test_parse_line_wo_time():
    '''Test parsing a line without price'''
    assert parse_line('P 2020-01-01 EUR 2.00 USD') == {
        'date': '2020-01-01',
        'time': None,
        'commodity': 'EUR',
        'amount': '2.00',
        'currency': 'USD'
    }
