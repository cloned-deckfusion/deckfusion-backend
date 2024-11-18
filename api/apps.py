# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ DJANGO IMPORTS
# └─────────────────────────────────────────────────────────────────────────────────────

from django.apps import AppConfig


# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ API CONFIG
# └─────────────────────────────────────────────────────────────────────────────────────


class ApiConfig(AppConfig):
    """API Config"""

    # Define name
    name = "api"

    # Define default auto field
    default_auto_field = "django.db.models.BigAutoField"
