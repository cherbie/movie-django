from moviedemo.apps.moviehub.data.models import Cinema

from typing import Iterator

def get_cinemas() -> Iterator[Cinema]:
    """Get list of cinemas"""
    return Cinema.objects.all().iterator()