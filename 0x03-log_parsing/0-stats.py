#!/usr/bin/python3
""" This is my problem :'v """
import sys
import re
import signal
from collections import OrderedDict


def search_items(line, s):
    """ Search the items to positionate """
    regexu = r"\s\d{3}\s\d{1,}"
    txt = re.search(regexu, line)
    word = txt.group()
    word = word[1:]

    regexd = r"\d{3}\s"
    left = re.search(regexd, word)

    code = left.group()
    code = code[:-1]

    regext = r"\s\d{1,}"
    right = re.search(regext, word)

    size = right.group()
    size = size[1:]
    size = int(size)

    add_code(code, s)

    return size


def add_code(code, codes):
    """ Count the status code """
    try:
        codes[code] += 1
    except KeyError:
        pass


def print_all(stat):
    """ Print all """
    stat = OrderedDict(stat)

    for key, value in stat.items():
        if value is not 0:
            print("{}: {}".format(key, value))


if __name__ == "__main__":
    status = {"200": 0, "301": 0, "400": 0, "401": 0,
              "403": 0, "404": 0, "405": 0, "500": 0}
    file_size = 0
    i = 0

    try:
        for lines in sys.stdin:
            file_size += search_items(lines, status)

            if i is not 0 and i % 9 == 0:
                print("File size: {:d}".format(file_size))
                print_all(status)

            i += 1
    except KeyboardInterrupt:
        pass
    finally:
        print("File size: {:d}".format(file_size))
        print_all(status)
        sys.exit(0)
