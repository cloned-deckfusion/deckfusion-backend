# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ DJANGO IMPORTS
# └─────────────────────────────────────────────────────────────────────────────────────

from rest_framework.permissions import BasePermission, SAFE_METHODS


# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ USER PERMISSION
# └─────────────────────────────────────────────────────────────────────────────────────


class UserPermission(BasePermission):

    # ┌─────────────────────────────────────────────────────────────────────────────────
    # │ CLASS ATTRIBUTES
    # └─────────────────────────────────────────────────────────────────────────────────

    # Define message
    message = "You are not allowed to perform this action."

    # ┌─────────────────────────────────────────────────────────────────────────────────
    # │ HAS OBJECT PERMISSION
    # └─────────────────────────────────────────────────────────────────────────────────

    def has_object_permission(self, request, view, obj):
        """Has Permission Method"""

        # Read permissions are allowed for any user
        if request.method in SAFE_METHODS:
            return True

        # Give write permissions to user
        return obj == request.user
