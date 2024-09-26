import configparser

config = configparser.RawConfigParser()
path = "E:\software testing\lectures\selenium_framework\configurations\config.ini"
config.read(path)


class ReadConfig:
    @staticmethod
    def getApplicationURL():
        url = config.get('common info', 'baseUrl')
        return url

    @staticmethod
    def getUserEmail():
        username = config.get('common info', 'username')
        return username

    @staticmethod
    def getpassword():
        password = config.get('common info', 'password')
        return password
