#!/bin/python
# Before running this script, start the API server:
#
# > bin\headless.exe --port=1234

import json
import requests

api = 'http://localhost:1234'
hours_to_sim = '12:00:00'

def main():
    # Make sure to start the simulation from the beginning
    print('Did you just start the simulation? Time is currently',
          requests.get(api + '/sim/get-time').text)

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
if __name__ == '__main__':
    main()
