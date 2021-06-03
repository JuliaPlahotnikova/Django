import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Vacancies_stepik.settings')

application = get_wsgi_application()
