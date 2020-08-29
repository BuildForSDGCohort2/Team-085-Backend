import os
# from sqlalchemy import Column, String, Integer
# from sqlalchemy import Boolean, DateTime, ARRAY, ForeignKey
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

# Database path is stored in the virtual environment
# with a key name of DATABASE_PATH
database_path = os.environ["DATABASE_PATH"]


"""
setup_db(app)
    binds a flask application and a SQLAlchemy service
"""


def setup_db(app):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    migrate.init_app(app, db)
    return db


"""
Users
    The table containing users and their personal details
"""


class Users(db.Model):
    __tablename__ = "Users"

    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(200), nullable=False)
    lastname = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    # Jobs relationship
    jobs = db.relationship("Jobs", backref="users", lazy=True)

    """
    Class Methods
    """

    """
    insert()
        Performs the C in CRUD
        inserts a new model into a database
        the model must have a unique id or null id
        EXAMPLE
            user = Users(firstname=req_firstname, lastname=req_lastname)
            user.insert()
    """
    def insert(self):
        db.session.add(self)
        db.session.commit()

    """
    update()
        Performs the U in CRUD
        updates an existing database model
        the model must exist in the database
        EXAMPLE
            user = Users.query.filter(Users.id == id).one_or_none()
            user.firstname = 'Lorem'
            user.update()
    """
    def update(self):
        db.session.commit()

    """
    delete()
        deletes an existing model from the database
        the model must exist in the database
        EXAMPLE
            user = Users(firstname=req_firstname, lastname=req_lastname)
            user.delete()
    """
    def delete(self):
        db.session.delete(self)
        db.session.commit()


"""
Jobs
    The table containing jobs that have been ordered \
    and their order details.

    Status:
        ordered(default) - indicates a client has placed an order.
        accepted - indicates the artisan has accepted the job.
        cancel_pending - Indicates one of the parties has requested to \
            annul the order, but the other party is yet to accept.
        cancelled - means either one of the parties annulled the order \
            and both parties have agreed to cancel.
        completed - indicates an order has been successfully completed.
"""


class Jobs(db.Model):
    __tablename__ = "Jobs"

    id = db.Column(db.Integer, primary_key=True)
    artisan_id = db.Column(db.Integer,
                           db.ForeignKey('Users.id'),
                           nullable=False)
    client_id = db.Column(db.Integer,
                          db.ForeignKey('Users.id'),
                          nullable=False)
    status = db.Column(db.String(120),
                       nullable=False,
                       default='ordered')

    """
    Class Methods
    """

    """
    insert()
        Performs the C in CRUD
        inserts a new model into a database
        the model must have a unique id or null id
        EXAMPLE
            job = Jobs(artisan_id=req_artisan_id, client_id=req_client_id)
            job.insert()
    """
    def insert(self):
        db.session.add(self)
        db.session.commit()

    """
    update()
        Performs the U in CRUD
        updates an existing database model
        the model must exist in the database
        EXAMPLE
            job = Jobs.query.filter(Jobs.id == id).one_or_none()
            job.status = 'completed'
            job.update()
    """
    def update(self):
        db.session.commit()

    """
    delete()
        deletes an existing model from the database
        the model must exist in the database
        EXAMPLE
            job = Jobs(artisan_id=req_artisan_id, client_id=req_client_id)
            job.delete()
    """
    def delete(self):
        db.session.delete(self)
        db.session.commit()
