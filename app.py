# import os
from flask import Flask
from models.models import setup_db

"""
App Config
    Creates the flask app
"""
app = Flask(__name__)
db = setup_db(app)

"""
Models
    Imports models from models/models.py file
    The reason the models are not being imported at the top is due to \
    errors that may arise from the models being created before the flask app
"""
from models.models import Users, Jobs

if __name__ == '__main__':
    app.run(port=8080, debug=True)
