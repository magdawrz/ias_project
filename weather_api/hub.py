from .providers.dark_sky import DarkSkyProvider
from .providers.openweathermap import OpenWeatherMapProvider
from .providers.exceptions import BaseProviderError


class WeatherHub:
    """
    Aggregate all providers in a single class.
    """
    def __init__(self, providers=None):
        self.providers = providers if providers is not None else []

    def register_provider(self, provider):
        """
        Register a new provider.

        :param provider: BaseProvider subclass
        """
        self.providers.append(provider)

    def current_weather(self, location: dict) -> list:
        """
        Get current weather from all providers.
        :param location: dictionary with latitude and longitute
        :return: a list of weathers from providers
        """
        data = []

        for provider in self.providers:
            try:
                current_weather = provider.current_weather(location=location)
                data.append({provider.NAME: current_weather})
            except BaseProviderError:
                data.append(
                    {
                        provider.NAME: {
                          'error': 'Cannot get data from provider'
                        }
                    }
                )

        return data


def weather_hub_fabric(configuration):
    return WeatherHub(providers=[
        DarkSkyProvider(api_key=configuration.DARK_SKY_API_KEY),
        OpenWeatherMapProvider(api_key=configuration.OPEN_WEATHER_MAP_API_KEY),
    ])
