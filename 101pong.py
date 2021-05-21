#!/usr/bin/python3
import sys
import math
from error_handling import *
from calculations import *


def pong():
    x1 = float(sys.argv[1])
    y1 = float(sys.argv[2])
    z1 = float(sys.argv[3])
    x2 = float(sys.argv[4])
    y2 = float(sys.argv[5])
    z2 = float(sys.argv[6])
    n = int(sys.argv[7])

    calc_vector(x1,x2, y1, y2, z1, z2)
    z = position_ball(x1, x2, y1, y2, z1, z2, n)
    verify = hit(z2, z, x1, x2)
    hit_bat(x1, x2, y1, y2, z1, z2, verify)


def main():
    error = rigor()
    if error != 0:
        exit(84)
    else:
        pong()
        exit (0)

main()