from flask_script import Manager

from config import ApplicationConfig
from weather_api import create_app


manager = Manager(create_app(ApplicationConfig))


if __name__ == '__main__':
    manager.run()
