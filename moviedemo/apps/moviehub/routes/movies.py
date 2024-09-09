from rest_framework import generics
from rest_framework.renderers import JSONRenderer

from moviehub.domain.movie import get_movies_currently_showing
from moviehub.utils import pagination
from moviehub.data.serializers import MovieSerializer
from moviehub.data import models

class _MovieAPIViewBase(generics.GenericAPIView):
    serializer_class = MovieSerializer
    queryset = models.Movie.objects.all()
    renderer_classes = [JSONRenderer]


class MovieListAPIView(generics.ListAPIView, pagination.ListModelMixin, _MovieAPIViewBase):
    pagination_class = pagination.StandardResultsSetPagination

    def get_queryset(self):
        return get_movies_currently_showing()


class _MovieRetrieveAPIView(generics.RetrieveAPIView, _MovieAPIViewBase):
    pass


class _MovieUpdateAPIView(generics.UpdateAPIView, _MovieAPIViewBase):
    pass


class _MovieCreateAPIView(generics.CreateAPIView, _MovieAPIViewBase):
    pass


class MovieDetailAPIView(_MovieRetrieveAPIView, _MovieUpdateAPIView, _MovieCreateAPIView):
    pass


__all__ = [MovieDetailAPIView, MovieListAPIView]