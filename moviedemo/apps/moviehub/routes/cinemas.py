from rest_framework import generics
from rest_framework.renderers import JSONRenderer

from moviehub.utils import pagination
from moviehub.data.serializers import CinemaSerializer
from moviehub.data import models

class _CinemaAPIViewBase(generics.GenericAPIView):
    serializer_class = CinemaSerializer
    queryset = models.Cinema.objects.all()
    renderer_classes = [JSONRenderer]


class CinemaListAPIView(generics.ListAPIView, pagination.ListModelMixin, _CinemaAPIViewBase):
    pagination_class = pagination.StandardResultsSetPagination


class _CinemaRetrieveAPIView(generics.RetrieveAPIView, _CinemaAPIViewBase):
    pass


class _CinemaUpdateAPIView(generics.UpdateAPIView, _CinemaAPIViewBase):
    pass


class _CinemaCreateAPIView(generics.CreateAPIView, _CinemaAPIViewBase):
    pass


class CinemaDetailAPIView(_CinemaRetrieveAPIView, _CinemaUpdateAPIView, _CinemaCreateAPIView):
    pass


__all__ = [CinemaDetailAPIView, CinemaListAPIView]