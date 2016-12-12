import os

import pytest


@pytest.fixture(scope='session')
def dark_sky_api_key():
    """
    Read Dark Sky api key from environmental variable DARK_SKY_API_KEY.
    :return: string
    """
    return os.environ.get('DARK_SKY_API_KEY')


@pytest.fixture(scope='session')
def open_weather_api_key():
    """
    Read Open Weather Map from environmental variable OPEN_WEATHER_MAP_API_KEY.
    :return: sting
    """
    return os.environ.get('OPEN_WEATHER_MAP_API_KEY')


@pytest.fixture(scope='session')
def location():
    return {
        'latitude': '51.107885',
        'longitude': '17.038538',
    }
