import logging
import inspect

class LogGenerator:

    @staticmethod
    def loggen():
        # to show class name(eg.Test_001_login) we use inspect and provide that variable in logger variable
        name = inspect.stack()[1][3]
        logger = logging.getLogger(name)
        file = logging.FileHandler("E:\\software testing\\lectures\\selenium_framework\\logs\\Automation_log1.log")
        format = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(funcName)s : %(lineno)s : %(message)s")
        file.setFormatter(format)
        logger.addHandler(file)
        logger.setLevel(logging.INFO)
        return logger

# class LogGen:
#     @staticmethod
#     def loggen():
#         logging.basicConfig(filename="logs\\CT10.log", format="%(asctime)s %(message)s", filemode='w')
#         logger = logging.getLogger()
#
#         logger.setLevel(logging.DEBUG)
#         return logger


