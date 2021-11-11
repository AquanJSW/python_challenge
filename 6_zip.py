#!/usr/bin/env python3
from zipfile import ZipFile
import codecs

FILE_PATH = './channel.zip'

def get_fname(n: int):
    return str(n) + '.txt'

def insight_file(zf: ZipFile, fname: str):
    if fname not in zf.namelist():
        print("FileNotExist: {}".format(fname))
        return False
    
    content = list(map(codecs.decode, zf.open(fname).readlines()))
    string = content[0].strip().split()[-1].removesuffix('\n')

    try:
        next_number = eval(string)
        return next_number
    except:
        print('{}\n{}'.format(fname, ''.join(content)))
        return False

if __name__ == '__main__':
    zf = ZipFile(FILE_PATH)
    
    max_iter = len(zf.namelist()) - 1

    fname = '90052.txt'

    for _ in range(max_iter):
        ans = insight_file(zf, fname)
        if ans:
            fname = get_fname(ans)
        else:
            break
