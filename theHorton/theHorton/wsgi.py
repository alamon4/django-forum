"""
WSGI config for theHorton project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
<<<<<<< HEAD
https://docs.djangoproject.com/en/1.7/howto/deployment/wsgi/
=======
https://docs.djangoproject.com/en/dev/howto/deployment/wsgi/
>>>>>>> 661e8000e9324155314cbca15c1c4bcb502acb6c
"""

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "theHorton.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
