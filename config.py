import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))


class Config(object):
    """
    Will be loaded by create_app in project/__init__.py

    Put all your config settings here
    and use environment variables for confidential data.

    NOTE: flask only load UPPERCASE keys.
    """

    SECRET_KEY = os.environ.get('SECRET_KEY')

    # put other configuration variables here
    # ex: LANGUAGES = ['en', 'fr']
