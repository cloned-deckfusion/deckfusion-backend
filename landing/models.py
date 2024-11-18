# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ DJANGO IMPORTS
# └─────────────────────────────────────────────────────────────────────────────────────

from django.conf import settings
from django.db import models

# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ PROJECT IMPORTS
# └─────────────────────────────────────────────────────────────────────────────────────

from utils.mixins.model_mixins import CommonModelMixin


# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ CONTACT MESSAGE
# └─────────────────────────────────────────────────────────────────────────────────────


class ContactMessage(CommonModelMixin):
    """Contact Message Model"""

    # ┌─────────────────────────────────────────────────────────────────────────────────
    # │ FIELDS
    # └─────────────────────────────────────────────────────────────────────────────────

    # Define user field
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="contact_messages",
    )

    # Define text field
    text = models.TextField()

    # ┌─────────────────────────────────────────────────────────────────────────────────
    # │ __STR__
    # └─────────────────────────────────────────────────────────────────────────────────

    def __str__(self) -> str:
        """String Method"""

        # Return name
        return (
            "Contact Message from "
            f"{self.user.first_name} {self.user.last_name} ({self.user.email})"
        )

    # ┌─────────────────────────────────────────────────────────────────────────────────
    # │ META
    # └─────────────────────────────────────────────────────────────────────────────────

    class Meta:
        """Meta Class"""

        # Define verbose names
        verbose_name = "Contact Message"
        verbose_name_plural = "Contact Messages"
