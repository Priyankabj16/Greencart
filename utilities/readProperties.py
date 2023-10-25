import configparser

config = configparser.RawConfigParser()
config.read(".\\Configurations\\config.ini")


class ReadConfig:
    @staticmethod
    def getbaseURL():
        baseURL = config.get('common info', 'baseUrl')
        return baseURL
