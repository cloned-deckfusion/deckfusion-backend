# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ GENERAL IMPORTS
# └─────────────────────────────────────────────────────────────────────────────────────

import os

# import scout_apm.celery

# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ CELERY IMPORTS
# └─────────────────────────────────────────────────────────────────────────────────────

from celery import Celery

# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ DJANGO ENVIRONMENT
# └─────────────────────────────────────────────────────────────────────────────────────

# Configure Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ CELERY APP
# └─────────────────────────────────────────────────────────────────────────────────────

# Initialize Celery app
app = Celery(
    "deckfusion",
)

# Load settings from Django settings
app.config_from_object("django.conf:settings", namespace="CELERY")

# Intall Scout Celery
# scout_apm.celery.install(app)

# Load tasks from all registered apps
app.autodiscover_tasks()
