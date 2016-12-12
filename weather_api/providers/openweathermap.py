"""
This module contain a provider class for OpenWeatherMap.
(http://api.openweathermap.org)
"""

import requests
from requests.exceptions import HTTPError

from .base import BaseProvider
from .exceptions import OpenWeatherMapConnectionError


class OpenWeatherMapProvider(BaseProvider):
    NAME = 'openweathermap'
    UNITS = 'metric'
    CURRENT_WEATHER_URI = (
       'http://api.openweathermap.org/data/2.5/weather?'
       'lat={latitude}&lon={longitude}&APPID={api_key}' + '&units=' + UNITS
    )

    def current_weather(self, location: dict) -> dict:
        """
        Get current weather from Open Weather Map.

        Raises OpenWeatherMapConnectionError when OWM returns response
        different than 200.

        :param location: a dictionary object containing two keys:
            latitude, longitude
        :return: a dictionary object
        """
        response = requests.get(
            self.CURRENT_WEATHER_URI.format(
                api_key=self.api_key,
                latitude=location['latitude'],
                longitude=location['longitude'],
            )
        )

        try:
            response.raise_for_status()
        except HTTPError as exc:
            raise OpenWeatherMapConnectionError from exc

        return self.normalize_current_weather(data=response.json())

    def normalize_current_weather(self, data):
        main = data.get('main')
        return {
            'temperature': main.get('temp'),
            'win_speed': data.get('wind', {}).get('speed'),
            'pressure': main.get('pressure'),
            'humidity': main.get('humidity'),
            'time': data.get('dt')
        }
