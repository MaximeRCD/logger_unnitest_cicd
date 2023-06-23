from modules.utility.date import getTodayString
from modules.logger.logs import Logger
if __name__ == "__main__":
    Logger.log.debug('Generating New Password')
    print(getTodayString())