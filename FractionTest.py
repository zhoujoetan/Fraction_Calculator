import unittest
from Fraction import *


class FractionTest(unittest.TestCase):

    def testZeroDivide(self):
        # Notice that assertRaises does not call Fraction directly!
        self.assertRaises(ZeroDivisionError, Fraction, 1, 0)
        
    def testMultiply(self):
        self.assertEqual(Fraction(3, 10),
                         Fraction(1, 2).multiply(Fraction(3, 5)))

    def testLessThan(self):
        self.assertTrue(Fraction(1, 100) < Fraction(1, 2))

    def testEqual(self):
        self.assertEqual(Fraction(1, 2), Fraction(1, 2))
        self.assertEqual(Fraction(1, 2), Fraction(3, 6))
        self.assertEqual(Fraction(-1, 2), Fraction(1, -2))
        self.assertEqual(Fraction(-1, -2), Fraction(1, 2))

    def testAdd(self):
    
        self.assertEqual(Fraction(1,4).add(Fraction(1,2)), Fraction(3,4))
        self.assertEqual(Fraction(1,2).add(Fraction(1,2)), Fraction(1,1))
        self.assertEqual(Fraction(3,4).add(Fraction(3,4)), Fraction(3,2))
        self.assertEqual(Fraction(3,4).add(Fraction(-1,2)), Fraction(1,4))
        self.assertEqual(Fraction(-1,4).add(Fraction(-1,2)), Fraction(3,-4))
        self.assertEqual(Fraction(1,4).add(Fraction(1,-4)), Fraction(0,1))
        self.assertEqual(Fraction(0,4).add(Fraction(0,-5)), Fraction(0,1))

    def testSubtract(self):
        self.assertEqual(Fraction(1,4).subtract(Fraction(1,2)), Fraction(1,-4))
        self.assertEqual(Fraction(1,2).subtract(Fraction(1,2)), Fraction(0,1))
        self.assertEqual(Fraction(3,4).subtract(Fraction(-3,4)), Fraction(3,2))
        self.assertEqual(Fraction(-3,4).subtract(Fraction(-1,2)), Fraction(-1,4))
        self.assertEqual(Fraction(-1,4).subtract(Fraction(1,-4)), Fraction(0,1))
        self.assertEqual(Fraction(1,4).subtract(Fraction(1,4)), Fraction(0,1))
        self.assertEqual(Fraction(0,4).subtract(Fraction(0,-5)), Fraction(0,1))

    def testDivide(self):
        self.assertEqual(Fraction(1, 2).divide(Fraction(3, 5)),Fraction(5,6))
        self.assertEqual(Fraction(0, 2).divide(Fraction(3, 5)),Fraction(0,1))
        self.assertEqual(Fraction(-1, 2).divide(Fraction(3, 5)),Fraction(5,-6))
        self.assertEqual(Fraction(1, 2).divide(Fraction(1,2)),Fraction(1,1))
        self.assertRaises(ZeroDivisionError, Fraction(1,-2).divide,Fraction(0,6))

    def testAbsValue(self):
        self.assertEqual(Fraction(-1, 2).absValue(), Fraction(1, 2))
        self.assertEqual(Fraction(1, 2).absValue(), Fraction(1, 2))
        self.assertEqual(Fraction(0, 2).absValue(), Fraction(0, 2))
        self.assertEqual(Fraction(0, -2).absValue(), Fraction(0, 2))
        self.assertEqual(Fraction(-1, -3).absValue(), Fraction(1, 3))

    def testNegate(self):
        self.assertEqual(Fraction(-1, 2).negate(), Fraction(1, 2))
        self.assertEqual(Fraction(1, 2).negate(), Fraction(-1, 2))
        self.assertEqual(Fraction(0, 2).negate(), Fraction(0, 2))
        self.assertEqual(Fraction(0, -2).negate(), Fraction(0, 2))
        self.assertEqual(Fraction(1, -2).negate(), Fraction(1, 2))
        self.assertEqual(Fraction(-1, -3).negate(), Fraction(-1, 3))
    def testString(self):
        self.assertEqual(Fraction(1,1).__str__(), "1")
        self.assertEqual(Fraction(10,1).__str__(), "10")
        self.assertEqual(Fraction(10,-1).__str__(), "-10")
        self.assertEqual(Fraction(0,1).__str__(), "0")
unittest.main()
