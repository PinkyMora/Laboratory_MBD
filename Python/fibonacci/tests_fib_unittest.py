import unittest

from fibonacci import fibonacci

class testFibonacciiterative(unittest.TestCase):
    
    def test_fibonacci_1_is_1(self):
        self.assertEqual(fibonacci(1),1)

    def test_fibonacci_9_is_34(self):
        self.assertEqual(fibonacci(9),34)  

    '''def test_fibonacci_negative(self):
        with self.assertRaises(ValueError):
            fibonacci(-1) 
    '''