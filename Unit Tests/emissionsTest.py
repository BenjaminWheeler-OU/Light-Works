import unittest
def emissionValidator(time_spent):
    """
    Validates the emission reduction based on the time spent at a traffic light.
    
    Rules:
    - Time must be a positive integer or float.
    - Excessively large values (e.g., > 100000) are considered invalid.
    - Non-numeric values should return False.
    """
    if not isinstance(time_spent, (int, float)):  # Ensure input is numeric
        return False
    if time_spent < 0:  # Time cannot be negative
        return False
    if time_spent > 100000:  # Arbitrary large limit for edge case
        return False
    return True  # Valid case
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
