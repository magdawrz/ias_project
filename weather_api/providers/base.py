"""
This module contain a base class that must be implemented by all providers.
"""
from abc import ABCMeta, abstractmethod


class BaseProvider(metaclass=ABCMeta):
    """
    Base class that must be implemented by all providers.
    """
    NAME = None
    CURRENT_WEATHER_URI = None

    def __init__(self, api_key):
        self.api_key = api_key

    @abstractmethod
    def current_weather(self, location: dict) -> dict:
        """
        Return current weather from providers.

        This method must return data normalized by method
            normalize_current_weather.

        Returned data structure is the same like in normalize_current_weather.
        :return: a dictionary object
        """

    @abstractmethod
    def normalize_current_weather(self, data) -> dict:
        """
        Normalize current weather returned from providers's API.

        This method must return data in the following format:
        {
            'temperature': float, temperature in celsius degrees
            'win_speed': float, wind speed in meters per hour
            'pressure': float, pressure in hectopascals
            'humidity': float, humidity in percents
            'time': time, UNIX timestamp
        }
        :return: a dictionary object
        """
