import os
import logging
from flask import Flask
from flask_bootstrap import Bootstrap
from config import Config, DevelopmentConfig
from logging.handlers import RotatingFileHandler

# app config
app = Flask(__name__)
app.config.from_object(DevelopmentConfig)
bootstrap = Bootstrap(app)

from app.errors import bp as errors_bp
app.register_blueprint(errors_bp)

from app.main import bp as main_bp
app.register_blueprint(main_bp)
    
#from app import routes

if not app.debug:
	if not os.path.exists('logs'):
		os.mkdir('logs')
		
	file_handler = RotatingFileHandler('logs/fizzbizz.log', maxBytes=10240, backupCount=10)
	file_handler.setFormatter(logging.Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
	file_handler.setLevel(logging.INFO)
	app.logger.addHandler(file_handler)

	app.logger.setLevel(logging.INFO)
	app.logger.info('FizzBizz startup')
