class PasswordVerifier:
    def __init__(self, password):
        self.password = password

    def is_secure(self):
        # Check for security requirements
        if len(self.password) < 8:
            return False

        has_uppercase = False
        has_lowercase = False
        has_digit = False
        has_special_char = False

        for char in self.password:
            if char.isupper():
                has_uppercase = True
            elif char.islower():
                has_lowercase = True
            elif char.isdigit():
                has_digit = True
            else:
                has_special_char = True

        return has_uppercase and has_lowercase and has_digit and has_special_char
