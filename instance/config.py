from os.path import abspath, dirname, realpath, join

class config(object):

    SECRET_KEY = ''
    SQLALCHEMY_DATABASE_URI = 'postgresql://proxyuser:password@127.0.0.1/testdb'

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    BASE_DIR = abspath(dirname(__file__))
    #UPLOAD_FOLDER = join(dirname(realpath(__file__)), '../microservice/static/uploads')

class prod_config(config):
    DEBUG = False

class dev_config(config):
    DEBUG = True

class test_config(config):
    TESTING = True