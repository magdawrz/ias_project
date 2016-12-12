import pytest

from ..providers.dark_sky import DarkSkyProvider

from .custom_assertions import assert_current_weather


@pytest.mark.integration
def test_get_current_weather_from_dark_sky(dark_sky_api_key, location):
    provider = DarkSkyProvider(api_key=dark_sky_api_key)
    current = provider.current_weather(location=location)
    assert_current_weather(current_weather=current)
