#!/usr/bin/env python3

import re

CONTENT_FILE_PATH = './3.txt'
RESULT_FILE_PATH = './3_result.txt'

regex = re.compile(r'[^A-Z][A-Z]{3}([a-z])[A-Z]{3}[^A-Z]')

if __name__ == '__main__':
    # read
    with open(CONTENT_FILE_PATH, 'r') as fp:
        # content = fp.readlines()  # keep new line
        # content = ''.join(content)
        content = ''
        for line in fp.readlines():
            content += line.removesuffix('\n')

    # find
    with open(RESULT_FILE_PATH, 'w') as fp:
        fp.write(''.join(regex.findall(content)))
