# Скопіюй цей код у WSGI configuration file на PythonAnywhere.
# Заміни YOUR_USERNAME на свій логін PythonAnywhere.

import os
import sys

PROJECT_HOME = "/home/YOUR_USERNAME/hw_25/task_2_push_notifications"

if PROJECT_HOME not in sys.path:
    sys.path.insert(0, PROJECT_HOME)

os.environ["DJANGO_SETTINGS_MODULE"] = "notification_project.settings"
os.environ["DJANGO_DEBUG"] = "False"
os.environ["PYTHONANYWHERE_DOMAIN"] = "YOUR_USERNAME.pythonanywhere.com"

from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()
