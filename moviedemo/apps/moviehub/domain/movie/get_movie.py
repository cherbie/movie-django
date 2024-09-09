from moviehub.data.models import Movie, Cinema
from moviehub.data.serializers import MovieSerializer, CinemaSerializer

from django.db.models.query import QuerySet
from typing import Iterator, Optional
import datetime

# TODO: need to figure out how querysets and the "domain" layer work together

def get_movie_details(movie_id: str) -> Optional[Movie]:
    """Get movie details"""
    try:
        return Movie.objects.get(id=movie_id)
    except Movie.DoesNotExist:
        return None


def get_movies_currently_showing() -> QuerySet:
    """Get list of currently showing movies"""
    return Movie.objects.all().filter(release_date__lte=datetime.datetime.now())
