import math

class InvalidInputError(Exception):
    def __init__(self, text):
        self.value = text

class Fraction:
    def __init__(self, numerator = 0, denominator = 1):
        self.numerator = numerator
        self.denominator = denominator

    def _simplify(self):
        '''Simplifies fractions to lowest form'''
        if self.numerator == self.denominator:
            return

        divisor = math.gcd(self.denominator, self.numerator)
        if self.numerator != 1 and divisor != 1: #Simplifies if the numerator divides the denominator or vice-versa
            self.denominator = self.denominator / divisor
            self.numerator = self.numerator / divisor
            return

        if (self.denominator < 0 and self.numerator > 0) or (self.denominator < 0 and self.numerator < 0): #Makes the number positive if the numerator and denominator are negative
            self.numerator = self.numerator * -1                                                           #or shifts the negative to the numerator if only the denominator is negative
            self.denominator = self.denominator * -1


    def _common_denom(self, other):
        '''Converts two numbers to have a common denominator before performing an operation'''
        Fraction._simplify(self)
        Fraction._simplify(other)

        if self.denominator == other.denominator:
            return
        
        lcd = abs(self.denominator * other.denominator) // math.gcd(self.denominator, other.denominator) #Finds the least common multiple of the two denominators
        
        multi = lcd / self.denominator          #Multiplies first fraction to have the same common denominator
        self.numerator = self.numerator * multi
        self.denominator = self.denominator * multi

        multi = lcd / other.denominator         #Multiplies other fraction to have the same common denominator
        other.numerator = other.numerator * multi
        other.denominator = other.denominator * multi


    def __add__(self, other):
        Fraction._common_denom(self, other)
        return Fraction(self.numerator + other.numerator, self.denominator)


    def __sub__(self, other):
        Fraction._common_denom(self, other)
        return Fraction(self.numerator - other.numerator, self.denominator)


    def __mul__(self, other):
        return Fraction(self.numerator * other.numerator, self.denominator * other.denominator)


    def __truediv__(self, other):
        return Fraction(self.numerator * other.denominator, self.denominator * other.numerator)


    def display(self):
        '''Prints the fraction in the proper format'''
        Fraction._simplify(self)
        print("%d/%d" % (self.numerator, self.denominator))


x = 0
while x != 'q':
    try:
        x = input("""Fraction Calculator\n\n+ - Add \n- - Subtract \n* - Multiple \n/ - Divide 
                  \nEnter which operation you'd like to execute (q to quit):\n""")
        if x not in ['+', '-', '*', '/', 'q']:
            raise InvalidInputError("No valid operator entered, try again")
        elif x == 'q':
            print("The program will now exit")
            continue
        print("Now enter the fractions for this operation Input syntax:(Fraction = n/d, Integer = x)")
        num1 = input("First: ")
        if num1.find('/') > -1:
            num1 = num1.split('/')
            if num1[0].lstrip('-').isdigit() and num1[1].lstrip('-').isdigit() and len(num1) == 2:
                num1 = Fraction(int(num1[0]), int(num1[1]))
            else:
                raise InvalidInputError("Entered values are not digits, please start again")
        elif num1.lstrip('-').isdigit():
            num1 = Fraction(int(num1), 1)
        else:
            raise InvalidInputError("No valid input entered, please start again")

        num2 = input("Second: ")
        if num2.find('/') > -1:
            num2 = num2.split('/')
            if num2[0].lstrip('-').isdigit() and num2[1].lstrip('-').isdigit() and len(num2) == 2:
                num2 = Fraction(int(num2[0]), int(num2[1]))
            else:
                raise InvalidInputError("Entered values are not digits, please start again")
        elif num2.lstrip('-').isdigit():
            num2 = Fraction(int(num2), 1)
        else:
            raise InvalidInputError("No valid input entered, please start again")

        answer = Fraction()
        if x == '+':
            answer = num1 + num2
        elif x == '-':
            answer = num1 - num2
        elif x == '*':
            answer = num1 * num2
        elif x == '/':
            answer = num1 / num2

        print("The result of your calculation is: ")
        answer.display()
        x = input("Enter q to quit or anything else to continue: ")

    except InvalidInputError as excpt_val:
        print(excpt_val)
