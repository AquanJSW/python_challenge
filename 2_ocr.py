#!/usr/bin/env python3

CONTENT_FILE_PATH = './2_ocr.txt'
RESULT_FILE_PATH = './2_ocr_result.txt'

if __name__ == '__main__':
    # statistic and
    # find unique chars' first occurence index
    with open(CONTENT_FILE_PATH, 'r') as fp:
        content = ''.join(fp.readlines())
        unique_chars = set(content)
        unique_chars_lindex = []
        statistic = {}
        for char in unique_chars:
            unique_chars_lindex.append(content.find(char))
            statistic[char] = content.count(char)

    statistic_with_lindex = zip(statistic.items(), unique_chars_lindex)

    # sort by lindex
    statistic = dict(sorted(statistic_with_lindex, key=lambda x: x[1])).keys()
    # sort by count
    statistic = sorted(statistic, key=lambda x: x[1])

    with open(RESULT_FILE_PATH, 'w') as fp:
        for k, v in statistic:
            line = '{}: {:5}'.format(k, v) + '\n'
            fp.write(line)
