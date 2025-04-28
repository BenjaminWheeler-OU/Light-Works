import unittest


def delete_user_data_secure(user_id, current_user_role):
    if current_user_role != 'admin':
        raise PermissionError("Unauthorized access: Only admins can delete user data.")
    print(f"User {user_id}'s data deleted.")
    return True

class TestAuthorization(unittest.TestCase):



    def test_vulnerable_function_allows_any_user(self):
        # Simulate a user with 'user' role deleting data (should NOT be allowed)
        result = delete_user_data_secure(user_id=1, current_user_role='user')
        self.assertTrue(result, "Vulnerable function allowed unauthorized access")

    def test_secure_function_blocks_unauthorized_user(self):
        with self.assertRaises(PermissionError):
            delete_user_data_secure(user_id=1, current_user_role='user')

    def test_secure_function_allows_admin(self):
        result = delete_user_data_secure(user_id=1, current_user_role='admin')
        self.assertTrue(result, "Secure function should allow admin access")

if __name__ == '__main__':
    unittest.main()
