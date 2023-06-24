import unittest
from rules.classes import PasswordVerifier


class PasswordVerifierTests(unittest.TestCase):
    def test_secure_password(self):
        password = "VerySecure123!"
        verifier = PasswordVerifier(password)
        self.assertTrue(verifier.is_secure())

    def test_insecure_password_short_length(self):
        password = "weak123"
        verifier = PasswordVerifier(password)
        self.assertFalse(verifier.is_secure())

    def test_insecure_password_no_uppercase(self):
        password = "weakpassword123!"
        verifier = PasswordVerifier(password)
        self.assertFalse(verifier.is_secure())

    def test_insecure_password_no_lowercase(self):
        password = "WEAKPASSWORD123!"
        verifier = PasswordVerifier(password)
        self.assertFalse(verifier.is_secure())

    def test_insecure_password_no_digit(self):
        password = "WeakPassword!"
        verifier = PasswordVerifier(password)
        self.assertFalse(verifier.is_secure())

    def test_insecure_password_no_special_char(self):
        password = "WeakPassword123"
        verifier = PasswordVerifier(password)
        self.assertFalse(verifier.is_secure())


if __name__ == "__main__":
    unittest.main()
