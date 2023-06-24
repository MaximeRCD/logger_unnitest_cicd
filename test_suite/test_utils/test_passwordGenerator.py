import unittest
from utils.password import PasswordGenerator
from rules.classes import PasswordVerifier


class PasswordGeneratorTests(unittest.TestCase):
    def test_generate_password_insecure(self):
        generator = PasswordGenerator()
        generator.secure = False
        password = generator.generate_password()
        verifier = PasswordVerifier(password)
        self.assertFalse(verifier.is_secure())

    def test_generate_password_secure(self):
        generator = PasswordGenerator()
        generator.secure = True
        password = generator.generate_password()
        verifier = PasswordVerifier(password)
        self.assertTrue(verifier.is_secure())


if __name__ == "__main__":
    unittest.main()
