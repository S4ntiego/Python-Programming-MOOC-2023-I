# Write your solution here
from math import sqrt


def hypotenuse(leg1: float, leg2: float):
    c = leg1 * leg1 + leg2 * leg2
    return sqrt(c)
