import os

class Config(object):
	DEBUG = False
	CSRF_ENABLED = True
	SECRET_KEY = os.getenv('SECRET_KEY')
	JWT_SECRET_KEY = os.getenv('JWT_SECRET')
	JWT_BLACKLIST_ENABLED = True
	JWT_BLACLIST_TOKEN_CHECKS = ['access', 'refresh']
	#REDIS_URL = 'redis://:{pw}@redis:6379/0'.format(pw=os.getenv('REDIS_PW'))


	# TODO: create secret key func and create secret key at creation if the file
	SQLALCHEMY_DATABASE_URI = 'sqlite:///../app.db'
	SQLALCHEMY_TRACK_MODIFICATIONS = False



class DevelopmentConfig(Config):
	"""Config for dev"""
	DEBUG = True

class TestingConfig(Config):
	"""Config for testing """

	DEBUG = True
	TESTING = True

	#TODO: change database to testing

class StageingConfig(Config):
	"""Config for stageing"""

	DEBUG = True

class ProductionConfig(Config):
	"""Config for production """

	DEBUG = False
	TESTING = False

app_config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'staging': StageingConfig,
    'production': ProductionConfig
}
