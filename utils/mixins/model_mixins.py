# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ DJANGO IMPORTS
# └─────────────────────────────────────────────────────────────────────────────────────

from django.db import models


# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ COMMON MODEL MIXIN
# └─────────────────────────────────────────────────────────────────────────────────────


class CommonModelMixin(models.Model):
    """An abstract model mixin with common fields that we'd want to use every time"""

    # ┌─────────────────────────────────────────────────────────────────────────────────
    # │ FIELDS
    # └─────────────────────────────────────────────────────────────────────────────────

    # Define created at field
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="created at")

    # Define update at field
    updated_at = models.DateTimeField(auto_now=True, verbose_name="updated at")

    # ┌─────────────────────────────────────────────────────────────────────────────────
    # │ META
    # └─────────────────────────────────────────────────────────────────────────────────

    class Meta:
        """Meta Class"""

        # Set abstract to True
        abstract = True
