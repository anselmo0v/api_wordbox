from os.path import abspath, dirname, realpath, join

class config(object):

    SECRET_KEY = '902ur0wejfwdncsdkncsd3nl54j5kf'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://wordbox:wordbox@localhost/wordbox'

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    BASE_DIR = abspath(dirname(__file__))

    DEBUG = False