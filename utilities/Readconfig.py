import configparser

config= configparser.RawConfigParser()
config.read(".\\Configuration\\config.ini")

class ReadConfig_Class:

    @staticmethod
    def getUsername():
        username= config.get('login data', 'username')
        return username

    @staticmethod
    def getPassword():
        password= config.get('login data', 'password')
        return password

