import unittest
from emissionTester import emissionValidator

class TestEmissionReduction(unittest.TestCase):
    def test_valid_emission_calculation(self):
        """Correct case: Emissions are calculated correctly in normal range"""
        self.assertTrue(emissionValidator(50))  # Assuming 50 is a valid input

    def test_invalid_non_numeric_input(self):
        """Incorrect case: Non-numeric input should fail"""
        self.assertFalse(emissionValidator("invalid"))

    def test_boundary_negative_time(self):
        """Boundary condition: Time spent at light cannot be negative"""
        self.assertFalse(emissionValidator(-1))

    def test_edge_large_time_value(self):
        """Edge case: Excessively large time value"""
        self.assertFalse(emissionValidator(10**6))  # Assuming an upper limit exists
        
if __name__ == '__main__':
    unittest.main()
