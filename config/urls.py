# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ DJANGO IMPORTS
# └─────────────────────────────────────────────────────────────────────────────────────

from django.conf import settings
from django.contrib import admin
from django.urls import path


# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ URL PATTERNS
# └─────────────────────────────────────────────────────────────────────────────────────

# Define URL patterns
urlpatterns = []

# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ DJANGO ADMIN
# └─────────────────────────────────────────────────────────────────────────────────────

# Admin URL Pattern
if settings.ENABLE_DJANGO_ADMIN:

    # Get environment title
    environment_title = settings.ENVIRONMENT.title()

    # Define title from environment reminder
    TITLE = f"DeckFusion {environment_title}"

    # Set title for Django Admin
    admin.site.site_title = TITLE
    admin.site.site_header = TITLE
    admin.site.index_title = "Admin Panel"

    # Add Django Admin URL patterns
    urlpatterns += [path("admin/", admin.site.urls)]
