import math

class Fraction:
    def __init__(self, numerator = 0, denominator = 1):
        self.numerator = numerator
        self.denominator = denominator

    def _simplify(self):
        '''Simplifies fractions to lowest form'''
        if self.numerator == self.denominator:
            return

        if self.denominator % self.numerator == 0:
            divisor = math.gcd(self.denominator, self.numerator)
            self.denominator = self.denominator / divisor
            self.numerator = self.numerator / divisor


    def _common_denom(self, other):
        '''Converts two numbers to have a common denominator before performing an operation'''
        if isinstance(other, int):
            other = Fraction(other * self.denominator, self.denominator)
            return
        
        _simplify(self)
        _simplify(other)

        if self.denominator == other.denominator:
            return
        
        lcd = abs(self.denominator * other.denominator) // math.gcd(self.denominator * other.denominator) #Finds the least common multiple of the two denominators
        
        multi = lcd / self.denominator          #Multiplies first fraction to have the same common denominator
        self.numerator = self.numerator * multi
        self.denominator = self.denominator * multi

        multi = lcd / other.denominator         #Multiplies other fraction to have the same common denominator
        other.numerator = other.numerator * multi
        other.denominator = other.denominator * multi


    def __add__(self, other):
        _common_denom(self, other)
        return Fraction(self.numerator + other.numerator, self.denominator)

    def __sub__(self, other):
        _common_denom(self, other)
        return Fraction(self.numerator + other.numerator, self.denominator)


    def __mul__(self, other):
        return Fraction(self.numerator * other.numerator, self.denominator * other.denominator)

    def __truediv__(self, other):
        return Fraction(self.numerator * other.denominator, self.denominator * other.numerator)

    def display(self):
        '''Prints the fraction in the proper format'''
        print("%d/%d" % (self.numerator, self.denominator))

