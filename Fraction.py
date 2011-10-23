def myGcd(a, b):
    while b != 0:
       t = b
       b = a % b
       a = t
    return a
        
class Fraction(object):

    def __init__(self, num, denom):
        """Initialize a Fraction object."""
        if denom == 0:
            raise ZeroDivisionError
        gcd = myGcd(num, denom)
        self.num = num // gcd
        self.denom = denom // gcd

    def __str__(self):
        """Return the string format of a Fraction object."""
        if (self.num == 0):
            self.denom = 1
        if self.denom == 1:
            return str(self.num)
        return str(self.num) + '/' + str(self.denom)

    def __eq__(self, other):
        """Define the equality of Fraction objects."""
        return self.num == other.num and self.denom == other.denom

    def __lt__(self, other):
        """Define the less than operation of Fraction objects."""
        return self.num * other.denom < other.num * self.denom
    
    def multiply(self, other):
        """Define the multiplication operation of Fraction objects."""
        num = self.num * other.num
        denom = self.denom * other.denom
        return Fraction(num, denom)


    def add(self, other):
        """Define the addition operation of Fraction objects."""
        num = self.num * other.denom + self.denom * other.num
        denom = other.denom * self.denom
        return Fraction(num,denom)

    def subtract(self, other):
        """Define the subtraction operation of Fraction objects."""
        num = self.num * other.denom - self.denom * other.num
        denom = other.denom * self.denom
        return Fraction(num,denom)

    def divide(self, other):
        """Define the division operation of Fraction objects."""
        num = self.num * other.denom
        denom = self.denom * other.num
        return Fraction(num,denom)

    def absValue(self):
        """Define the absolute operation of a Fraction object."""
        if self.num * self.denom < 0:
            num = -self.num
        else:
            num = self.num
        denom = self.denom
        return Fraction(num,denom)

    def negate(self):
        """Define the negation operation of a Fraction object."""
        num = -self.num
        denom = self.denom
        return Fraction(num,denom)


    
