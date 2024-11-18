# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ GENERAL IMPORTS
# └─────────────────────────────────────────────────────────────────────────────────────

from __future__ import annotations

from typing import Any, TypeVar

# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ DJANGO IMPORTS
# └─────────────────────────────────────────────────────────────────────────────────────

from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models

# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ PROJECT IMPORTS
# └─────────────────────────────────────────────────────────────────────────────────────

from utils.functions.normalizers import normalize_email


# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ USER MANAGER
# └─────────────────────────────────────────────────────────────────────────────────────

UserClass = TypeVar("UserClass", bound=AbstractUser)


class UserManager(BaseUserManager[UserClass]):
    """A custom user manager that uses email instead of username"""

    # ┌─────────────────────────────────────────────────────────────────────────────────
    # │ CLASS ATTRIBUTES
    # └─────────────────────────────────────────────────────────────────────────────────

    # Enable this manager for migrations
    use_in_migrations = True

    # ┌─────────────────────────────────────────────────────────────────────────────────
    # │ CREATE USER
    # └─────────────────────────────────────────────────────────────────────────────────

    def create_user(
        self, email: str, password: str | None = None, **kwargs: Any
    ) -> UserClass:
        """Creates and saves a regular user given an email and password"""

        # Check if email is null
        if not email:
            # Raise ValueError
            raise ValueError("Users must have a valid email address")

        # Normalize the email address
        email = self.normalize_email(email)

        # Create user instance
        user = self.model(email=email, **kwargs)

        # Set user password
        user.set_password(password)

        # Save user to database
        user.save(using=self._db)

        # Return user instance
        return user

    # ┌─────────────────────────────────────────────────────────────────────────────────
    # │ CREATE SUPERUSER
    # └─────────────────────────────────────────────────────────────────────────────────

    def create_superuser(self, email: str, password: str, **kwargs: Any) -> UserClass:
        """Creates and saves a superuser given an email and password"""

        # Ensure that user is staff and superuser
        kwargs.setdefault("is_staff", True)
        kwargs.setdefault("is_superuser", True)

        # Create the super user instance
        superuser = self.create_user(email, password, **kwargs)

        # Return the superuser instance
        return superuser

    # ┌─────────────────────────────────────────────────────────────────────────────────
    # │ GET BY NATURAL KEY
    # └─────────────────────────────────────────────────────────────────────────────────

    def get_by_natural_key(self, email: str | None) -> UserClass:
        """Ensures that email is case insensitive when authenticating"""

        # Get by case-insensitive email
        return self.get(email__iexact=email)


# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ USER
# └─────────────────────────────────────────────────────────────────────────────────────


class User(AbstractUser):
    """A custom user model that uses email instead of username"""

    # ┌─────────────────────────────────────────────────────────────────────────────────
    # │ EMAIL
    # └─────────────────────────────────────────────────────────────────────────────────

    # Nullify username field
    username = None  # type: ignore

    # Define email field
    email: models.EmailField[Any, str] = models.EmailField(
        unique=True, max_length=255, db_index=True
    )

    # Set username field to email
    USERNAME_FIELD = "email"

    # Define required fields
    REQUIRED_FIELDS = []

    # ┌─────────────────────────────────────────────────────────────────────────────────
    # │ MODEL MANAGER
    # └─────────────────────────────────────────────────────────────────────────────────

    # Use the custom model manager
    objects: UserManager[User] = UserManager()

    # ┌─────────────────────────────────────────────────────────────────────────────────
    # │ __STR__
    # └─────────────────────────────────────────────────────────────────────────────────

    def __str__(self) -> str:
        """String Method"""

        # Return email
        return self.email

    # ┌─────────────────────────────────────────────────────────────────────────────────
    # │ SAVE
    # └─────────────────────────────────────────────────────────────────────────────────

    def save(self, *args: Any, **kwargs: Any) -> None:
        """Save Method"""

        # Emailize the email address
        # i.e. lowercase, no special characters, no spaces
        self.email = normalize_email(self.email)

        # Save object
        return super().save(*args, **kwargs)

    # ┌─────────────────────────────────────────────────────────────────────────────────
    # │ META
    # └─────────────────────────────────────────────────────────────────────────────────

    class Meta:
        """Meta Class"""

        # Define verbose names
        verbose_name = "User"
        verbose_name_plural = "Users"
