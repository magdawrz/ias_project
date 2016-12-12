class BaseProviderError(Exception):
    pass


class DarkSkyConnectionError(BaseProviderError):
    pass


class OpenWeatherMapConnectionError(BaseProviderError):
    pass
