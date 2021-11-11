#!/usr/bin/env python3

import pickle
from urllib import request

if __name__ == '__main__':
    banner = request.urlopen('http://www.pythonchallenge.com/pc/def/banner.p').read()
    deserialized = pickle.loads(banner)
    for line in deserialized:
        for char_count in line:
            print(char_count[0] * char_count[1], end='')
        print()

"""
Wrong
"""
# import copy
# from tqdm import tqdm

# DATA_PATH = './4.txt'


# class Seq:
#     def __init__(self, seq):
#         self.__seq = copy.deepcopy(seq)
#         self.__comp_seq = self.__get_comp_seq()

#     def get_peaks(self, side_adjacency: int=2):
#         ans = []
#         i = 0
#         s = self.__comp_seq
#         bar = tqdm(total=len(s) - 2 * side_adjacency)
#         while i < len(s) - 2 * side_adjacency:
#             bar.update(i)
#             for _ in range(side_adjacency):
#                 i += 1
#                 if s[i]:
#                     break
#             else:
#                 for _ in range(side_adjacency):
#                     i += 1
#                     if not s[i]:
#                         break
#                 else:
#                     ans.append(self.__seq[i - side_adjacency])
#         return ans

#     def __get_comp_seq(self):
#         """
#         return `list[bool]`: Is greater than last?
#         """
#         ans = []
#         for i in range(1, len(self.__seq)):
#             ans.append(self.__seq[i] > self.__seq[i-1])
#         return ans


# if __name__ == '__main__':
#     with open(DATA_PATH) as fp:
#         numbers = tuple(
#             map(lambda x: eval(x.removesuffix('\n')), fp.readlines()))
#     seq = Seq(numbers)
#     print(seq.get_peaks(3))
