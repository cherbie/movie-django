from rest_framework.pagination import PageNumberPagination
from rest_framework import mixins, response

class StandardResultsSetPagination(PageNumberPagination):
    """Sensible pagination defaults.
    """
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 25


class ListModelMixin(mixins.ListModelMixin):
    """List a queryset.
    """
    def list(self, _request, *_args, **_kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        serializer = (self.get_serializer(page, many=True) if page is not None else self.get_serializer(queryset, many=True))

        response_data = self.get_paginated_response(serializer.data)
        return response.Response(response_data)