import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    #security
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'XKFNTFzDzG3DaEWqg5R*5BG6V5P54YtHF5wS@9JCrMLMr9wYha3Gj^PMyq7bpWp%s@cD!'
    #database
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    #email error reporting
    MAIL_SERVER = os.environ.get('MAIL_SERVER')
    MAIL_PORT = int(os.environ.get('MAIL_PORT') or 25)
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') is not None
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    #list of admins to get error notifications - add to list as needed
    ADMINS = ['dhruvbatra2@gmail.com']