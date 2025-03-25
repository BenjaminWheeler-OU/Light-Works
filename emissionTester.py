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

if __name__ == "__main__":
    # Sample test cases
    print(emissionValidator(50))       # Expected: True
    print(emissionValidator("invalid")) # Expected: False
    print(emissionValidator(-1))       # Expected: False
    print(emissionValidator(10**6))    # Expected: False
