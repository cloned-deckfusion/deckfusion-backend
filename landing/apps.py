# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ DJANGO IMPORTS
# └─────────────────────────────────────────────────────────────────────────────────────

from django.apps import AppConfig


# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ LANDING CONFIG
# └─────────────────────────────────────────────────────────────────────────────────────


class LandingConfig(AppConfig):
    """Landing Config"""

    # Define name
    name = "landing"

    # Define default auto field
    default_auto_field = "django.db.models.BigAutoField"
