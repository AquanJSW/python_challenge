#!/usr/bin/env python3
"""
g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj.
"""

def caesar(c, offset):
    base = ord('a') if c.islower() else ord('A')
    return chr(base + (ord(c) - base + offset) % 26)


def getlines():
    ans = ''
    try:
        for line in iter(input, ''):
            ans += line + '\n'
    except EOFError:
        pass
    return ans[:-1]

def main():
    print("input origin:")
    origin = getlines()
    offset = eval(input("offset: "))
    encrypted = ""
    for c in origin:
        if not c.isalpha():
            encrypted += c
            continue
        encrypted += caesar(c, offset)
    print(encrypted)
    str.maketrans


if __name__ == '__main__':
    main()
