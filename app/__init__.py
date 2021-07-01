from flask import Flask
from flask_restx import Api


app = Flask(__name__)

api = Api(app,
            version='1.0',
            title='Bot Facebook Graph',
            description='webhook facebook',
            prefix='/api/',
            doc='/docs/')