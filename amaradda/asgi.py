"""
ASGI config for Amar Adda project.
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'amaradda.settings')

application = get_asgi_application()
