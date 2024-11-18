# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ DJANGO IMPORTS
# └─────────────────────────────────────────────────────────────────────────────────────

from rest_framework import serializers


# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ USER EMAIL SERIALIZER
# └─────────────────────────────────────────────────────────────────────────────────────


class UserEmailSerializer(serializers.Serializer):
    """User Email Serializer"""

    # Define email field
    email = serializers.EmailField(required=True)
