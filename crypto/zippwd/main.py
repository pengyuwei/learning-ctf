#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# coding=utf8

# 22dc8822  src1.txt
# dbf02445  src2.txt

import binascii
import string
import time

zipcrc = []


def check(crcstr):
    for i in zipcrc:
        if i == crcstr:
            return True


def main():
    success = 0
    all = len(zipcrc)
    for a in string.printable:
        for b in string.printable:
            for c in string.printable:
                for d in string.printable:
                    crc = a+b+c+d
                    crcstr = binascii.crc32(str.encode(crc))
                    if check(crcstr):
                        success += 1
                        print(crc)
                        if success >= all:
                            return

if __name__ == '__main__':
    zipcrc.append(0xd1f4eb9a)
    zipcrc.append(0xa6669d7d)
    zipcrc.append(0x19a07b3c)
    t = time.time()
    main()
    print("spend time: %ds" % (time.time() - t))
