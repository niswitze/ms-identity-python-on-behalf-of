#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
from dotenv import load_dotenv


def main():

    if os.environ.get("ENVIRONMENT").lower() == "development":
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'UI.development_settings')
        load_dotenv(".\development.env")
    elif os.environ.get("ENVIRONMENT").lower() == "production":
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'UI.production_settings')
        load_dotenv(".\production.env")
    else:
        raise Exception("No ENVIRONMENT variable set")
        
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc   

    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
