# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ DJANGO IMPORTS
# └─────────────────────────────────────────────────────────────────────────────────────

from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from dynamic_rest.serializers import DynamicModelSerializer
from rest_framework import serializers

# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ PROJECT IMPORTS
# └─────────────────────────────────────────────────────────────────────────────────────

from user.models import User


# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ USER EMAIL SERIALIZER
# └─────────────────────────────────────────────────────────────────────────────────────


class UserEmailSerializer(serializers.Serializer):
    """User Email Serializer"""

    # Define email field
    email = serializers.EmailField(required=True)


# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ USER SERIALIZER
# └─────────────────────────────────────────────────────────────────────────────────────


class UserSerializer(DynamicModelSerializer):
    """User Serializer"""

    # ┌─────────────────────────────────────────────────────────────────────────────────
    # │ META
    # └─────────────────────────────────────────────────────────────────────────────────

    class Meta:
        """Meta Class"""

        # ┌─────────────────────────────────────────────────────────────────────────────
        # │ MODEL
        # └─────────────────────────────────────────────────────────────────────────────

        # Define model class
        model = User

        # Define model name
        name = "user"

        # ┌─────────────────────────────────────────────────────────────────────────────
        # │ FIELDS
        # └─────────────────────────────────────────────────────────────────────────────

        # Define fields
        fields = (
            "id",
            "email",
            "first_name",
            "last_name",
            "password",
        )

        # Define extra keyword arguments
        extra_kwargs = {
            "password": {"write_only": True, "required": False},
            "active_at": {"read_only": True},
        }

    # ┌─────────────────────────────────────────────────────────────────────────────────
    # │ CREATE
    # └─────────────────────────────────────────────────────────────────────────────────

    def create(self, validated_data):
        """Create Method"""

        # Get password
        password = validated_data.pop("password", None) or ""

        # Validate password
        try:
            validate_password(password)

        # Handle ValidationError
        except ValidationError as e:
            raise serializers.ValidationError({"password": list(e.messages)})

        # Check if password is empty
        if not password.strip():

            # Raise ValidationError
            raise serializers.ValidationError(
                {"password": ["Password must contain characters other than spaces."]}
            )

        # Create user
        user = User.objects.create(**validated_data)

        # Set password
        user.set_password(password)

        # Save user
        user.save()

        # Return user
        return user

    # ┌─────────────────────────────────────────────────────────────────────────────────
    # │ UPDATE
    # └─────────────────────────────────────────────────────────────────────────────────

    def update(self, instance, validated_data):
        """Update Method"""

        # Get username
        username = validated_data.get("username", None)

        # Initialize try except
        try:
            # Unavailable
            unavailable = (
                User.objects.filter(username__iexact=username)
                .exclude(id=instance.id)
                .exists()
            )
        except Exception:
            raise serializers.ValidationError(
                {"username": ["Please try another username."]}
            )

        # Check if username is taken
        if unavailable:

            # Raise a validation error
            raise serializers.ValidationError(
                {"username": ["A user with that username already exists."]}
            )

        # Get password
        password = validated_data.pop("password", None)

        # Update instance
        instance = super().update(instance, validated_data)

        # Check if password is not null
        if password:

            # Validate password
            try:
                validate_password(password)

            # Handle ValidationError
            except ValidationError as e:
                raise serializers.ValidationError({"password": list(e.messages)})

            # Check if password is empty
            if not password.strip():

                # Raise a ValidationError
                raise serializers.ValidationError(
                    {
                        "password": [
                            "Password must contain characters other than spaces."
                        ]
                    }
                )

            # Set password
            instance.set_password(password)

        # Save instance
        instance.save()

        # Return instance
        return instance
