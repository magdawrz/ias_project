import os


class ApplicationConfig:
    DARK_SKY_API_KEY = None

    @classmethod
    def read_from_environment(cls):
        cls.DARK_SKY_API_KEY = os.environ.get('DARK_SKY_API_KEY')
        cls.OPEN_WEATHER_MAP_API_KEY = os.environ.get(
            'OPEN_WEATHER_MAP_API_KEY',
        )


ApplicationConfig.read_from_environment()
