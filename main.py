'''
    Import ledger prices and convert to beancount price format.
    It performs in-place conversion within the same directory.
    It will create a new file with the same name as the original file,
    but with a .beancount extension.
'''

import argparse
import re


def get_source_directory():
    ''' get the source directory from the command line '''
    # read command line arguments
    parser = argparse.ArgumentParser(description='Convert ledger prices to beancount prices')
    parser.add_argument('--src', type=str, help='the source directory')
    args = parser.parse_args()

    # return the source directory
    return args.src


def parse_line(line: str):
    ''' Parse a line of ledger prices file.
     Return the price object. '''
    # parse the line
    regex = r'P (\d{4}-\d{2}-\d{2})(?:\s+(\d{2}:\d{2}:\d{2}))?\s+([A-Z_]+)\s+([0-9.]+)\s+([A-Z]+)'
    match = re.match(regex, line)
    if not match:
        return None

    date = match.group(1)
    time = match.group(2)
    commodity = match.group(3)
    amount = match.group(4)
    currency = match.group(5)

    return {
        'date': date,
        'time': time,
        'commodity': commodity,
        'amount': amount,
        'currency': currency
    }


def main():
    ''' entry point '''
    # read command line arguments
    source_directory = get_source_directory()
    # todo read each file in the given directory
    for filename in os.listdir(source_directory):
        # read each line
        with open(filename, 'r') as f:
            for line in f:
                # todo convert to beancount format
                pass


if __name__ == "__main__":
    main()
