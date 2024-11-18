# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ DJANGO IMPORTS
# └─────────────────────────────────────────────────────────────────────────────────────

from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ PROJECT IMPORTS
# └─────────────────────────────────────────────────────────────────────────────────────

from user.models import User
from user.permissions import UserPermission
from user.serializers import UserSerializer
from user.utils.functions.getters import get_visible_users
from utils.classes.pagination import DynamicPagination
from utils.classes.viewsets import DynamicModelViewSet


# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ USER VIEW SET
# └─────────────────────────────────────────────────────────────────────────────────────


class UserViewSet(DynamicModelViewSet):
    """User ViewSet"""

    # ┌─────────────────────────────────────────────────────────────────────────────────
    # │ CLASS ATTRIBUTES
    # └─────────────────────────────────────────────────────────────────────────────────

    # Define model
    model = User

    # Define serializer class
    serializer_class = UserSerializer

    # Define pagination class
    pagination_class = DynamicPagination

    # Define permission classes
    permission_classes = [IsAuthenticated, UserPermission]

    # Define search fields
    search_fields = ["email", "first_name", "last_name"]

    # ┌─────────────────────────────────────────────────────────────────────────────────
    # │ CREATE
    # └─────────────────────────────────────────────────────────────────────────────────

    def create(self, request, *args, **kwargs):
        """Create Method"""

        # Get serializer
        serializer = self.get_serializer(data=request.data)

        # Return 400 respose  if serializer is invalid
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        # Save user
        serializer.save()

        # Return 201 response
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    # ┌─────────────────────────────────────────────────────────────────────────────────
    # │ GET OBJECT
    # └─────────────────────────────────────────────────────────────────────────────────

    def get_object(self):
        """Get Object Method"""

        # Get queryset
        queryset = self.filter_queryset(self.get_queryset())

        # Get lookup URL kwarg
        lookup_url_kwarg = self.lookup_url_kwarg or self.lookup_field

        # Check if lookup not present
        if lookup_url_kwarg not in self.kwargs:

            # Return a 404 page by default
            return get_object_or_404(queryset, **{"pk": "0"})

        # Get lookup
        lookup = self.kwargs[lookup_url_kwarg].lower()

        # Check if lookup is "me"
        if lookup == "me":
            return self.request.user

        # Get object
        obj = get_object_or_404(queryset, **{"pk": lookup})

        # Chec object permissions
        self.check_object_permissions(self.request, obj)

        # Return object
        return obj

    # ┌─────────────────────────────────────────────────────────────────────────────────
    # │ GET PERMISSIONS
    # └─────────────────────────────────────────────────────────────────────────────────

    def get_permissions(self):
        """Get Permissions Method"""

        # Return default permissions
        return super().get_permissions()

    # ┌─────────────────────────────────────────────────────────────────────────────────
    # │ GET QUERYSET
    # └─────────────────────────────────────────────────────────────────────────────────

    def get_queryset(self):
        """Get Queryset Method"""

        # Return queryset
        return get_visible_users(self.request.user).order_by("id")

    # ┌─────────────────────────────────────────────────────────────────────────────────
    # │ GET SERIALIZER CLASS
    # └─────────────────────────────────────────────────────────────────────────────────

    def get_serializer_class(self):
        """Get Serializer Class Method"""

        # Return super method
        return super().get_serializer_class()
