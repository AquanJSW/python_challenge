#!/usr/bin/env python3

import codecs
from urllib import request
from tqdm import tqdm

BASE_URL = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing='
ROOT_NOTHING = '12345'
LOOPS = 400
LOG_PATH = './4.txt'


def get_next_nothing(msg: bytes):
    return codecs.decode(msg).split()[-1]


if __name__ == '__main__':
    next_nothing = ROOT_NOTHING

    with open(LOG_PATH, 'w') as fp:
        for i in tqdm(range(LOOPS)):
            fp.write('{:3}: {}\n'.format(i, next_nothing))
            next_nothing = get_next_nothing(
                request.urlopen(BASE_URL+next_nothing).read())
