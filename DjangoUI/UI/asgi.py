"""
ASGI config for DjangoUI project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/asgi/
"""

import os
from dotenv import load_dotenv

from django.core.asgi import get_asgi_application

if os.environ.get("ENVIRONMENT").lower() == "development":
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'UI.development_settings')
    load_dotenv("..\development.env")
elif os.environ.get("ENVIRONMENT").lower() == "production":
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'UI.production_settings')
    load_dotenv("..\production.env")
else:
    raise Exception("No ENVIRONMENT variable set")

application = get_asgi_application()
