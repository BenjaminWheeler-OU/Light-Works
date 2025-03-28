import unittest
from statistics import mean

def average_time_spent_at_stoplight(wait_times):
    if not wait_times:
        return 0  # Return 0 if there are no wait times to avoid division by zero
    return mean(wait_times)

class TestAverageTimeSpentAtStoplight(unittest.TestCase):
    
    def test_typical_case(self):
        self.assertAlmostEqual(average_time_spent_at_stoplight([30, 45, 60]), 45.0)
    
    def test_single_value(self):
        self.assertAlmostEqual(average_time_spent_at_stoplight([50]), 50.0)
    
    def test_large_numbers(self):
        self.assertAlmostEqual(average_time_spent_at_stoplight([1000, 2000, 3000]), 2000.0)
    
    def test_zero_wait_times(self):
        self.assertAlmostEqual(average_time_spent_at_stoplight([0, 0, 0]), 0.0)
    
    def test_empty_list(self):
        self.assertAlmostEqual(average_time_spent_at_stoplight([]), 0.0)
    
    def test_mixed_values(self):
        self.assertAlmostEqual(average_time_spent_at_stoplight([10, 20, 30, 40, 50]), 30.0)
    
    def test_negative_values(self):
        with self.assertRaises(ValueError):
            average_time_spent_at_stoplight([-10, 20, 30])

if __name__ == "__main__":
    unittest.main()