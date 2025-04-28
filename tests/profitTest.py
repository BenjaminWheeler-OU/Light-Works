import math
import unittest

def profit_is_valid(profit):
    return isinstance(profit, (int, float)) and math.isfinite(profit)

class TestProfitValidation(unittest.TestCase):
    def test_correct_profit(self):
        self.assertTrue(profit_is_valid(100.50))  # Positive profit
        self.assertTrue(profit_is_valid(-50.75))  # Negative profit
    
    def test_incorrect_profit(self):
        self.assertFalse(profit_is_valid(float('nan')))  # Not a number
        self.assertFalse(profit_is_valid(float('inf')))  # Infinite profit
        self.assertFalse(profit_is_valid("100"))  # String instead of number
    
    def test_edge_cases(self):
        self.assertTrue(profit_is_valid(0.0))  # Neutral profit case

if __name__ == "__main__":
    unittest.main()