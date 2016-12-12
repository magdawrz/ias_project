"""
This module contain a provider class for DarkSky (https://darksky.net/dev/).
"""
import requests
from requests.exceptions import HTTPError

from .base import BaseProvider
from .exceptions import DarkSkyConnectionError


__all__ = ['DarkSkyProvider', ]


class DarkSkyProvider(BaseProvider):
    # Please read the dark sky documentation for units
    UNITS = 'si'
    CURRENT_WEATHER_URI = (
        'https://api.darksky.net/forecast/{api_key}/'
        '{latitude},{longitude}?units=' + UNITS
    )
    NAME = 'dark_sky'

    def current_weather(self, location: dict) -> dict:
        """
        Get current weather from DarkSky.

        Raises DarkSkyConnectionError when DarkSky returns response different
        than 200.

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
            raise DarkSkyConnectionError from exc

        return self.normalize_current_weather(data=response.json())

    def normalize_current_weather(self, data):
        current = data.get('currently', {})
        return {
            'temperature': current.get('temperature'),
            'win_speed': current.get('windSpeed'),
            'pressure': current.get('pressure'),
            'humidity': current.get('humidity', 0) * 100,
            'time': current.get('time')
        }
