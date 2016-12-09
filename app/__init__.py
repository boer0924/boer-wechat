from flask import Flask
from config import config


def create_app(config_name):
    app = Flask(__name__)

    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    from .wechat import wechat as wechat_blueprint
    from .admin import admin as admin_blueprint
    app.register_blueprint(wechat_blueprint)
    app.register_blueprint(admin_blueprint)

    return app
