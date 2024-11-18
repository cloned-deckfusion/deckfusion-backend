# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ PROJECT IMPORTS
# └─────────────────────────────────────────────────────────────────────────────────────

from user.models import User


# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ GET VISIBLE USERS
# └─────────────────────────────────────────────────────────────────────────────────────


def get_visible_users(user):
    """Get all visible users to a given user"""

    # Get user
    if isinstance(user, str) or isinstance(user, int):

        # Get user instance
        user = User.objects.filter(id=user).first()

    # Check if user is None
    if user is None:
        return User.objects.filter(id=0)

    # Check if superuser
    if user.is_superuser:
        return User.objects.all()

    # Return visible users
    return User.objects.filter(id=user.id)
