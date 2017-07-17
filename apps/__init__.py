from flask import Flask

from apps import dmt as dmt_blueprint, auth as auth_blueprint


def start_app(config_name):
    app = Flask(__name__)

    app.config.from_object(config_name)

    app.register_blueprint(dmt_blueprint.dmt)
    app.register_blueprint(auth_blueprint.auth, url_prefix='/v1/user/api')
    return app
