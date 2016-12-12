from flask_restful import reqparse, Resource

from config import ApplicationConfig
from .hub import weather_hub_fabric


weather_hub = weather_hub_fabric(ApplicationConfig)


class CurrentWeatherResource(Resource):

    @staticmethod
    def parse_request_args():
        parser = reqparse.RequestParser(trim=True)
        parser.add_argument('latitude', type=str, required=True)
        parser.add_argument('longitude', type=str, required=True)
        return parser.parse_args()

    def get(self):
        arguments = self.parse_request_args()
        return weather_hub.current_weather(location={
            'latitude': arguments.latitude,
            'longitude': arguments.longitude,
        })
