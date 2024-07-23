import configparser
def read_configuration(category, key):
    config = configparser.ConfigParser()
    config.read("configuration,config.ini")
    return config.get(category, key)
