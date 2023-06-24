from dates.functions import *
from logs.define import Logger

main_logger = Logger("logs/files/main_logs.log")
main_logger.debug("Printing a date")
main_logger.debug(substract_days(today(), 3))
main_logger.debug("Date printed")
