
from whitenoise.django import DjangoWhiteNoise
import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bookmarks.settings')

application = get_wsgi_application()
application = DjangoWhiteNoise(application)
