import unittest
import re

def is_strong_password(password):
    """
    Validate if a password meets strong password criteria:
    - At least 12 characters long
    - Contains at least one uppercase letter
    - Contains at least one lowercase letter
    - Contains at least one digit
    - Contains at least one special character (@#$%^&+=!)
    """
    if len(password) < 12:
        return False
    if not re.search(r"[A-Z]", password):
        return False
    if not re.search(r"[a-z]", password):
        return False
    if not re.search(r"[0-9]", password):
        return False
    if not re.search(r"[@#$%^&+=!]", password):
        return False
    return True

class TestPasswordPolicy(unittest.TestCase):
    def test_strong_password_valid(self):
        """Test that a valid strong password is accepted."""
        valid_password = "SecureP@ssw0rd123"
        self.assertTrue(is_strong_password(valid_password), 
                        f"Password '{valid_password}' should be valid")

    def test_password_too_short(self):
        """Test that a password shorter than 12 characters is rejected."""
        short_password = "Pass@1"
        self.assertFalse(is_strong_password(short_password), 
                         f"Password '{short_password}' should be rejected (too short)")

    def test_password_no_uppercase(self):
        """Test that a password without uppercase letters is rejected."""
        no_upper_password = "securep@ssw0rd123"
        self.assertFalse(is_strong_password(no_upper_password), 
                         f"Password '{no_upper_password}' should be rejected (no uppercase)")

    def test_password_no_lowercase(self):
        """Test that a password without lowercase letters is rejected."""
        no_lower_password = "SECUREP@SSW0RD123"
        self.assertFalse(is_strong_password(no_lower_password), 
                         f"Password '{no_lower_password}' should be rejected (no lowercase)")

    def test_password_no_digit(self):
        """Test that a password without digits is rejected."""
        no_digit_password = "SecureP@ssword"
        self.assertFalse(is_strong_password(no_digit_password), 
                         f"Password '{no_digit_password}' should be rejected (no digit)")

    def test_password_no_special_char(self):
        """Test that a password without special characters is rejected."""
        no_special_password = "SecurePassword123"
        self.assertFalse(is_strong_password(no_special_password), 
                         f"Password '{no_special_password}' should be rejected (no special char)")

if __name__ == "__main__":
    unittest.main()