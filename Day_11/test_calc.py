'''Python program to explore the 'unittest' module'''
import unittest
import calc

class TestCalc(unittest.TestCase):
    def test_add(self):
        self.assertEqual(calc.add(10,5),15)
        self.assertEqual(calc.add(-3,4),1)
        self.assertEqual(calc.add(-3,-4),-7)
    def test_subtract(self):
        self.assertEqual(calc.subtract(10,5),5)
        self.assertEqual(calc.subtract(-3,4),-7)
        self.assertEqual(calc.subtract(-3,-4),1)
    def test_multiply(self):
        self.assertEqual(calc.multiply(10,5),50)
        self.assertEqual(calc.multiply(-3,4),-12)
        self.assertEqual(calc.multiply(-3,-4),12)
    def test_divide(self):
        self.assertEqual(calc.divide(10,5),2)
        self.assertEqual(calc.divide(-3,4),-1)
        self.assertEqual(calc.divide(-3,-4),0)
        self.assertRaises(ValueError,calc.divide,10,0)
        with self.assertRaises(ValueError):
            calc.divide(10,0)

'''You need to add the below lines if you are executing this script from the command
line using 'python test_calc.py' -> meaning python interpreter checks the if condition
and then calls the unittest.main() method to execute the testcases.
Alternatively you can execute the script by using 'python -m unittest test_calc.py' ->
meaning you want to add unittest module to your env path and run its main method on 
test_calc.py, which will execute the defined testcases.'''
if __name__=="__main__":
    unittest.main()
