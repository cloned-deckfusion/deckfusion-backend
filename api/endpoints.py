# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ DJANGO IMPORTS
# └─────────────────────────────────────────────────────────────────────────────────────

from django.urls import path
from dynamic_rest.routers import DynamicRouter
from rest_framework_nested.routers import NestedDefaultRouter

# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ PROJECT IMPORTS
# └─────────────────────────────────────────────────────────────────────────────────────

from landing.views import EarlyAccessView
from user.views import UserViewSet


# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ API ROUTER
# └─────────────────────────────────────────────────────────────────────────────────────

# api_root (/)
router = DynamicRouter()

# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ USER
# └─────────────────────────────────────────────────────────────────────────────────────

# users/
router.register("users", UserViewSet, base_name="users")

# Define users router
users_router = NestedDefaultRouter(router, "users", lookup="user")

# ┌────────────────────────────────────────────────────────────────────────────────────┐
# │ URL PATTERNS                                                                       │
# └────────────────────────────────────────────────────────────────────────────────────┘

# Initialize URL patterns list
urlpatterns = [
    path("landing/early-access/", EarlyAccessView.as_view(), name="early_access"),
]

# Define router URLs
router_urls = [
    # Router urls
    router.urls,
    # Nested router urls
    users_router.urls,
]

# Concatenate all lists
for router_url in router_urls:
    urlpatterns += router_url
