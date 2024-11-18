# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ DJANGO IMPORTS
# └─────────────────────────────────────────────────────────────────────────────────────

from rest_framework import serializers


# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ CONTACT SERIALIZER
# └─────────────────────────────────────────────────────────────────────────────────────


class ContactSerializer(serializers.Serializer):
    """Contact Serializer"""

    # Define name fields
    first_name = serializers.CharField(max_length=255, required=True)
    last_name = serializers.CharField(max_length=255, required=True)

    # Define email field
    email = serializers.EmailField(required=True)

    # Define message field
    message = serializers.CharField(required=True)
