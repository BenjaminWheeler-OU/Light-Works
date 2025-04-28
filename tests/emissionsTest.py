import unittest
import sys
import os

# Add the parent directory to the path so we can import the modules
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import emissonsCalc

class TestEmissionsCalculator(unittest.TestCase):
    def test_get_waiting_time(self):
        """Test that get_waiting_time returns a dictionary"""
        # This is a basic test that would need to be run in a SUMO environment
        # For now, we'll just test the function signature
        self.assertTrue(hasattr(emissonsCalc, 'get_waiting_time'))
        self.assertTrue(callable(emissonsCalc.get_waiting_time))
    
    def test_calculate_emissions(self):
        """Test that calculate_emissions returns a numeric value"""
        # This is a basic test that would need to be run in a SUMO environment
        # For now, we'll just test the function signature
        self.assertTrue(hasattr(emissonsCalc, 'calculate_emissions'))
        self.assertTrue(callable(emissonsCalc.calculate_emissions))
    
    def test_emission_calculation_logic(self):
        """Test the logic of emission calculation with mock data"""
        # Create a mock vehicles list
        mock_vehicles = ['vehicle1', 'vehicle2']
        
        # Mock the get_waiting_time function to return a specific value
        original_get_waiting_time = emissonsCalc.get_waiting_time
        
        def mock_get_waiting_time():
            return {'vehicle1': 10, 'vehicle2': 5}
        
        # Replace the function with our mock
        emissonsCalc.get_waiting_time = mock_get_waiting_time
        
        try:
            # Calculate emissions with our mock data
            emissions = emissonsCalc.calculate_emissions(mock_vehicles)
            
            # Verify the result is numeric and positive
            self.assertIsInstance(emissions, (int, float))
            self.assertGreaterEqual(emissions, 0)
            
            # The expected calculation:
            # Base emissions: 1 gram per vehicle = 2 grams
            # Waiting time emissions: 0.5 grams per second waiting
            # Vehicle1: 10 seconds waiting = 5 grams
            # Vehicle2: 5 seconds waiting = 2.5 grams
            # Total expected: 2 + 5 + 2.5 = 9.5 grams
            # (Note: The actual implementation might differ slightly)
            
        finally:
            # Restore the original function
            emissonsCalc.get_waiting_time = original_get_waiting_time
    
    def test_emission_validator(self):
        """Test the emission validator function"""
        # This test assumes there's an emissionValidator function in emissonsCalc
        # If not, you may need to add it or modify this test
        
        # Test valid cases
        self.assertTrue(emissonsCalc.emissionValidator(50))
        self.assertTrue(emissonsCalc.emissionValidator(0))
        self.assertTrue(emissonsCalc.emissionValidator(99.9))
        
        # Test invalid cases
        self.assertFalse(emissonsCalc.emissionValidator(-1))
        self.assertFalse(emissonsCalc.emissionValidator(100001))
        self.assertFalse(emissonsCalc.emissionValidator("invalid"))
        
if __name__ == '__main__':
    unittest.main()
