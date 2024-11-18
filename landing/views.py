# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ DJANGO IMPORTS
# └─────────────────────────────────────────────────────────────────────────────────────

from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ PROJECT IMPORTS
# └─────────────────────────────────────────────────────────────────────────────────────

from user.models import User
from user.serializers import UserEmailSerializer


# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ EARLY ACCESS VIEW
# └─────────────────────────────────────────────────────────────────────────────────────


class EarlyAccessView(APIView):
    """Early Access View"""

    # ┌─────────────────────────────────────────────────────────────────────────────────
    # │ POST
    # └─────────────────────────────────────────────────────────────────────────────────

    def post(self, request, *args, **kwargs):
        """Post Method"""

        # Get serializer
        serializer = UserEmailSerializer(data=request.data)

        # Check if serializer is not valid
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        # Get email
        email = serializer.validated_data["email"]

        # Get or create user
        user, created = User.objects.get_or_create(email=email)

        # Get status
        _status = status.HTTP_201_CREATED if created else status.HTTP_200_OK

        # Get message
        message = "User created" if created else "User exists"

        # Return response
        return Response(
            {"message": message},
            status=_status,
        )
