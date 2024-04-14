import unittest

def check_email(email: str) -> bool:
    if '@' and ('.') in email and (' ') not in email:
        result = True
    else:
        result = False
    return result

class TestCheckEmail(unittest.TestCase):

    def test_valid_email(self):
        self.assertTrue(check_email('test@example.com'))

    def test_valid_email_with_hyphen(self):
        self.assertTrue(check_email('test-user@example.com'))

    def test_valid_email_with_multiple_dots(self):
        self.assertTrue(check_email('test.user@example.co.uk'))

    def test_invalid_email_without_at_symbol(self):
        self.assertFalse(check_email('testexample.com'))

    def test_invalid_email_without_dot(self):
        self.assertFalse(check_email('test@examplecom'))

    def test_invalid_email_with_space(self):
        self.assertFalse(check_email('test @example.com'))

if __name__ == '__main__':
    unittest.main()
