# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ DJANGO IMPORTS
# └─────────────────────────────────────────────────────────────────────────────────────

from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
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
    # │ CLASS ATTRIBUTES
    # └─────────────────────────────────────────────────────────────────────────────────

    # Define permission classes
    permission_classes = [AllowAny]

    # ┌─────────────────────────────────────────────────────────────────────────────────
    # │ GET SERIALIZER CLASS
    # └─────────────────────────────────────────────────────────────────────────────────

    def get_serializer_class(self):
        """Get Serializer Class Method"""

        # Return serializer
        return UserEmailSerializer

    # ┌─────────────────────────────────────────────────────────────────────────────────
    # │ POST
    # └─────────────────────────────────────────────────────────────────────────────────

    def post(self, request, *args, **kwargs):
        """Post Method"""

        # Get serializer class
        SerializerClass = self.get_serializer_class()

        # Get serializer
        serializer = SerializerClass(data=request.data)

        # Check if serializer is not valid
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        # Get email
        email = serializer.validated_data["email"]

        # Get or create user
        _, created = User.objects.get_or_create(email=email)

        # Get status
        _status = status.HTTP_201_CREATED if created else status.HTTP_200_OK

        # Get message
        message = "User created" if created else "User exists"

        # Return response
        return Response(
            {"message": message},
            status=_status,
        )
