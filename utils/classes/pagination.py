# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ DJANGO REST FRAMEWORK IMPORTS
# └─────────────────────────────────────────────────────────────────────────────────────

from dynamic_rest.pagination import DynamicPageNumberPagination
from rest_framework.exceptions import NotFound


# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ DYNAMIC PAGINATION
# └─────────────────────────────────────────────────────────────────────────────────────


class DynamicPagination(DynamicPageNumberPagination):
    """A dynamic pagination class for querysets"""

    # ┌─────────────────────────────────────────────────────────────────────────────────
    # │ CLASS ATTRIBUTES
    # └─────────────────────────────────────────────────────────────────────────────────

    # Define page size and max page size
    page_size = 20
    max_page_size = 1000

    # Define page query params
    page_query_param = "page"
    page_size_query_param = "page_size"

    # ┌─────────────────────────────────────────────────────────────────────────────────
    # │ GET PAGE METADATA
    # └─────────────────────────────────────────────────────────────────────────────────

    def get_page_metadata(self):
        """Constructs the metadata for the paginated response"""

        # Return page metadata
        return {
            self.page_query_param: self.page.number,
            self.page_size_query_param: self.get_page_size(self.request),
            "page_count": self.page.paginator.num_pages,
            "result_count": self.page.paginator.count,
        }

    # ┌─────────────────────────────────────────────────────────────────────────────────
    # │ GET PAGE NUMBER
    # └─────────────────────────────────────────────────────────────────────────────────

    def get_page_number(self, request, paginator):
        """Get Page Number Method"""

        # Get the original page number from the request
        page_number = request.query_params.get(self.page_query_param, 1)

        # Initialize try-except block
        try:
            # Convert page number to integer
            page_number = int(page_number)

        # Handle ValueError
        except ValueError:
            raise NotFound("Page number must be an integer.")

        # Handle negative page number "indexes"
        if page_number < 0:
            page_number = paginator.num_pages + page_number + 1

        # Ensure the page number is valid
        if page_number < 1 or page_number > paginator.num_pages:
            raise NotFound("Page number out of range.")

        # Return page number
        return page_number
