from django.contrib.admin import site

from .data.models import Cinema, Movie, MovieScreening

site.register(Movie)
site.register(Cinema)
site.register(MovieScreening)