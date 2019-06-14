# project/__init__.py

from flask import Flask
from config import Config


def create_app(config_class=Config):
    """
    Application factory, creates and configure the Flask application.
    """

    app = Flask(__name__)
    app.config.from_object(config_class)

    # a simple page that show all config variables
    @app.route('/')
    def hello():
        from flask import render_template
        return render_template('index.html', config=app.config)

    return app
