import pytest

from ..providers.openweathermap import OpenWeatherMapProvider

from .custom_assertions import assert_current_weather


@pytest.mark.integration
def test_get_current_weather_open_weather_map(open_weather_api_key, location):
    provider = OpenWeatherMapProvider(api_key=open_weather_api_key)
    current = provider.current_weather(location=location)
    assert_current_weather(current_weather=current)
