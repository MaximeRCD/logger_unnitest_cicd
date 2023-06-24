import unittest
from loguru import logger
from logs.define import Logger


class LoggerTests(unittest.TestCase):
    def setUp(self):
        # Set up the Logger instance for testing
        self.log_file = "test_log.log"
        self.logger = Logger(self.log_file)

    def tearDown(self):
        # Get the handler ID of the log file
        logger.remove(self.logger.handler_id)

    def test_info(self):
        message = "This is an informational message"
        self.logger.info(message)
        # Assert that the log file contains the expected message
        self.assertLogContains(message)

    def test_warning(self):
        message = "This is a warning message"
        self.logger.warning(message)
        # Assert that the log file contains the expected message
        self.assertLogContains(message)

    def test_error(self):
        message = "This is an error message"
        self.logger.error(message)
        # Assert that the log file contains the expected message
        self.assertLogContains(message)

    def test_debug(self):
        message = "This is a debug message"
        self.logger.debug(message)
        # Assert that the log file contains the expected message
        self.assertLogContains(message)

    def assertLogContains(self, message):
        # Read the contents of the log file
        with open(self.log_file, "r") as file:
            log_contents = file.read()
        # Assert that the message is present in the log contents
        self.assertIn(message, log_contents)


if __name__ == "__main__":
    unittest.main()
