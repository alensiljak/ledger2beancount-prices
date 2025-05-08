'''
    Import ledger prices and convert to beancount price format.
    It performs in-place conversion within the same directory.
    It will create a new file with the same name as the original file,
    but with a .beancount extension.
'''

import argparse
import os
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
    # read each file in the given directory
    for filename in os.listdir(source_directory):
        if not filename.endswith('.ledger'):
            continue

        prices = []
        # read each line
        source = os.path.join(source_directory, filename)
        with open(source, 'r', encoding='utf-8') as f:
            print(f'Processing {source}')

            for line in f:
                # convert to beancount format
                price = parse_line(line)
                if price:
                    prices.append(price)
                else:
                    # price not parsed, write the line as is
                    print(f'Warning: line not parsed: {line}')

        # write the converted prices to a new file
        destination = os.path.join(source_directory, filename.replace('.ledger', '.beancount'))
        with open(destination, 'w', encoding='utf-8') as f:
            for price in prices:
                time_str = price['time'] if price['time'] else ''
                f.write(f'{price["date"]} {time_str} price {price["commodity"]} {price["amount"]} {price["currency"]}\n')


if __name__ == "__main__":
    main()
