import random
import string
import time

from rules.classes import PasswordVerifier
from logs.define import Logger


class PasswordGenerator:
    def __init__(self):
        self.secure = True if random.randint(1, 2) % 2 == 0 else False
        self.password_length = (
            random.randint(12, 20) if self.secure else random.randint(3, 11)
        )
        self.logger = Logger("logs/files/paswwordGenerator_logs.log")

    def set_password_length(self, length):
        self.password_length = length

    def generate_password(self):
        characters = string.ascii_letters + string.digits + string.punctuation

        if not self.secure:
            # Generate insecure password with only lowercase letters
            return "".join(
                random.choices(string.ascii_lowercase, k=self.password_length)
            )
        else:
            # Generate secure password with a mix of characters
            password = ""
            verif = PasswordVerifier(password)
            while not verif.is_secure():
                verif.password = "".join(
                    random.choices(characters, k=self.password_length)
                )
                self.logger.info(
                    f"{verif.password} --> password secure ? {verif.is_secure()}"
                )
                self.logger.info(f"Sleeping for 5 sec ...")
                time.sleep(5)
            return verif.password
