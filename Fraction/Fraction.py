import math

class Fraction:
    def __init__(self, numerator = 0, denominator = 1):
        self.numerator = numerator
        self.denominator = denominator

    def _common_denom(self, other):
        '''Converts two numbers to a common denominator before performing an operation'''
        lowest = math.gcd(self.denominator, other.denominator)


    def _simplify(self):

    def __add__(self, other):

    def __sub__(self, other):

    def __mul__(self, other):

    def __truediv__(self, other):
