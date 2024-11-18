# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ GENERAL IMPORTS
# └─────────────────────────────────────────────────────────────────────────────────────

import os
import scout_apm.celery
import ssl

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
    broker_use_ssl={"ssl_cert_reqs": ssl.CERT_NONE},
    redis_backend_use_ssl={"ssl_cert_reqs": ssl.CERT_NONE},
)
app.config_from_object("django.conf:settings")

# Intall Scout Celery
scout_apm.celery.install(app)

# Load tasks from all registered apps
app.autodiscover_tasks()
