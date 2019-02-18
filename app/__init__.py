"""Instantiate an instance of the app."""

from flask import Flask
from app.api.v1.party.view import party_Blueprint
from app.api.v1.office.view import office_Blueprint
from app.api.v2.users.view import user_blueprint
from app.api.v2.office.view import office_blueprint
from app.api.v2.party.view import party_blueprint
from app.api.v2.candidates.view import candidate_blueprint
from app.api.v2.votes.view import votes_blueprint


def create_app():
    """create an instance of the flask app given the passed environment variable and return."""

    # instantiate the app
    app = Flask(__name__, instance_relative_config=True)
    
    # url prefix for api version 1
    version1 = "/api/v1"
        # url prefix for api version 2
    version2 = "/api/v2"
    # register party blueprint
    app.register_blueprint(party_Blueprint, url_prefix=version1)
    app.register_blueprint(office_Blueprint, url_prefix=version1)
    #v2
    app.register_blueprint(user_blueprint,url_prefix=version2)
    app.register_blueprint(office_blueprint, url_prefix=version2)
    app.register_blueprint(party_blueprint, url_prefix=version2)
    app.register_blueprint(candidate_blueprint, url_prefix=version2)
    app.register_blueprint(votes_blueprint, url_prefix=version2)


    return app

