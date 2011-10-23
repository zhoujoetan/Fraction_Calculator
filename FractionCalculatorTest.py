from FractionCalculator import *
import unittest

class FractionCalculatorTest(unittest.TestCase):
    def testEvaluate(self):
        self.assertEqual(evaluate(Fraction(0,1),"1 + 2 * 3  / 2"),Fraction(9,2))
        self.assertEqual(evaluate(Fraction(2,1),"1 + 2 * 3  / 2"),Fraction(9,2))
        self.assertEqual(evaluate(Fraction(1,1)," + 2 * 3  / 2"),Fraction(9,2))
        self.assertEqual(evaluate(Fraction(2,1),"1 + 2/3 * 3/4 / 1/2"),Fraction(5,2))
        self.assertEqual(evaluate(Fraction(-2,1),"-1/-2 + -2/5 * 3  / 2"),Fraction(3,20))
        self.assertEqual(evaluate(Fraction(-2,1),"1/2 2/3 3/4 4/5 -1/-2 + -2/5 * 3  / 2"),
                         Fraction(3,20))
        self.assertEqual(evaluate(Fraction(-2,1),"1 + 2 + 1/3 / 2/3 cat 1/2 2/3 3/4 4/5 -1/-2 + -2/5 * 3  / 2"),
                         Fraction(3,20))
        self.assertEqual(evaluate(Fraction(-2,1),"1/2 2/3 3/4 4/5 -1/-2 + -2/5 * 3  / 2"),
                         Fraction(3,20))
        self.assertEqual(evaluate(Fraction(-2,1),"+ -2/1 a + 3/1 * 2"), Fraction(28, 2))
        self.assertEqual(evaluate(Fraction(-2,1),"+ -2/1 n + 3/1 * 2"), Fraction(28, 2))               
        self.assertRaises(ValueError, evaluate, Fraction(0,1), "1 +* 2 * 3  / 2")
        self.assertRaises(EOFError, evaluate, Fraction(0,1), "1 + 2 * q 3  / 2")
        self.assertRaises(EOFError, evaluate, Fraction(0,1), "1 + 2/3 q / 2")
        self.assertRaises(ZeroDivisionError, evaluate, Fraction(0,1), "1 + 2 * 3  / 0")
        self.assertRaises(ValueError, evaluate, Fraction(0,1), "1 + rstu2 * 3  / 2")
        self.assertRaises(ValueError, evaluate, Fraction(0,1), "1 +#%$* 2 * 3  / 2")        
unittest.main()
