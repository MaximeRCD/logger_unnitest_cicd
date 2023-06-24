from loguru import logger


class Logger:
    def __init__(self, log_file):
        self.Logger = logger
        self.handler_id = self.Logger.add(log_file, rotation="500 MB", level="DEBUG")

    def info(self, message):
        self.Logger.info(message)

    def warning(self, message):
        self.Logger.warning(message)

    def error(self, message):
        self.Logger.error(message)

    def debug(self, message):
        self.Logger.debug(message)
