# import os
from flask import Flask
# from models.models import setup_db

"""
App Config
    Creates the flask app
"""


app = Flask(__name__)

if __name__ == '__main__':
    # app.run(port=8080, debug=True) => Development only
    app.run(port=8080)  # Production
