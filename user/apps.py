# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ DJANGO IMPORTS
# └─────────────────────────────────────────────────────────────────────────────────────

from django.apps import AppConfig


# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ USER CONFIG
# └─────────────────────────────────────────────────────────────────────────────────────


class UserConfig(AppConfig):
    """User Config"""

    # Define name
    name = "user"

    # Define default auto field
    default_auto_field = "django.db.models.BigAutoField"
