# config.py

class Config(object):
	"""
	@brief      Class for configuration.
	"""

	# Put any configurations here that are common across all environments

class DeveleopmentConfig(Config):
	"""
	@brief      Class for develeopment configuration.
	"""

	DEBUG = True
	SQLALCHEMY_ECHO = True

class ProductionConfig(Config):
	"""
	@brief      Class for production configuration.
	"""

	DEBUG = False

app_config = {
	'development': DeveleopmentConfig,
	'production': ProductionConfig
}
