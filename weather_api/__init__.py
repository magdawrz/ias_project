from flask import Flask, render_template
from flask_restful import Api

from .api import CurrentWeatherResource


def create_app(configuration):
    """
    Create flask application instance.

    :param configuration: configuration class object
    :return: a new Flask application
    """
    app = Flask(__name__)
    app.config.from_object(configuration)

    weather_api = Api(app)
    weather_api.add_resource(CurrentWeatherResource, '/api/weather/current')

    @app.route('/')
    def index():
        return render_template('index.html')

    return app
