#!/usr/bin/env python3
import zipfile

FILE_PATH = './channel.zip'

def get_fname(n: int):
    return str(n) + '.txt'

def insight_file(fname: str):
    try:
        with open(fname) as fp:
            string = fp.readline().split()[-1].removesuffix('\n')
    except:
        print("FileNotFoundError: {}".format(fname))
        return False

    try:
        next_number = eval(string)
        return next_number
    except:
        with open(fname) as fp:
            print(fname, fp.readlines())
        return False

if __name__ == '__main__':
    os.chdir(DIR)
    files = os.listdir()
    max_iter = len(files) - 1
    fname = '90052.txt'
    for _ in range(max_iter):
        ans = insight_file(fname)
        if ans:
            fname = get_fname(ans)
        else:
            break