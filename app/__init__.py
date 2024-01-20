from flask import Flask
from config import Config

app_variable = Flask(__name__)
app_variable.config.from_object(Config)

from app import routes
