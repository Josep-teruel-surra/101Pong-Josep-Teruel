#!/usr/bin/python3

import sys
import math


def calc_vector(x1, x2, y1, y2, z1, z2):
    x = x2 - x1
    y = y2 - y1
    z = z2 - z1
    print ("The velocity vector of the ball is:")
    print ("(%.2f, %.2f, %.2f)" % (x, y, z))


def position_ball(x1, x2, y1, y2, z1, z2, n):
    t = n
    n = n + 1
    x = (x2 - x1) * n + x1
    y = (y2 - y1) * n + y1
    z = (z2 - z1) * n + z1
    print ("At time t + %d, ball coordinates will be:" % t)
    print ("(%.2f, %.2f, %.2f)" % (x, y, z))
    return z


def hit_bat(x1, x2, y1, y2, z1, z2, verify):

    if verify == 1:
        print ("The ball won't reach the paddle")
    else:
        x = x2 - x1
        y = y2 - y1
        z = z2 - z1
        v = (x * x + y * y + z * z)
        norm = math.sqrt(v)
        print ("The incidence angle is:")
        angle = (z2 - z1) / norm
        angle = math.asin(angle)
        angle = math.degrees(angle)
        angle = abs(angle)
        print("%.2f" % angle)


def hit(z2, z, x1, x2):
    verify = 0

    if z2 > 0 and z >= 0:
        verify = 1
    if z2 < 0 and z <= 0:
      verify = 1
    if x1 == x2:
        verify = 1
    return verify