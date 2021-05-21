#!/usr/bin/python3

import sys
import math
from message import usage


def try_int(nb):
    try:
        int(nb)
    except ValueError:
        return False
    else:
        return True


def try_float(nb):
    try:
        float(nb)
    except ValueError:
        return False
    else:
        return True


def diff_floats():
    
    i = 1
    while i != 7:
        if try_float(sys.argv[i]):
            i = i + 1
        else:
            return 84
    return 0


def rigor():
    if len(sys.argv) == 2 and sys.argv[1] == "-h":
        usage()
        return 84
    elif len(sys.argv) < 8 or len(sys.argv) > 8:
        print("Error: Incorrect length of arguments")
        return 84
    if diff_floats() == 84:
        print("Error: Incorrect argument")
        return 84
    if not try_int(sys.argv[7]):
        print("Error: Incorrect argument")
        return 84
    if int(sys.argv[7]) + 1 < 0:
        print("Error: Incorrect argument")
        return 84
    return 0