from django.db import models

class AppModelBase(models.Model):
    class Meta:
        app_label = 'moviehub'
        abstract = True


class Cinema(AppModelBase):
    """Cinema details"""
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64, )
    location = models.CharField(max_length=200, )


class Movie(AppModelBase):
    """Movie details"""
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=128, )
    release_date = models.DateField()
    genre = models.CharField(max_length=64, )
    runtime = models.IntegerField()
    synopsis = models.TextField()
    director = models.CharField(max_length=64, )
    rating = models.CharField(max_length=8, )
    princess_theatre_id = models.CharField(max_length=16,)
    cinema = models.ForeignKey(Cinema, on_delete=models.CASCADE)


class MovieScreening(AppModelBase):
    """Movie screening details within a cinema"""
    id = models.AutoField(primary_key=True)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    cinema = models.ForeignKey(Cinema, on_delete=models.CASCADE)
    showtime = models.DateTimeField()
    ticket_price = models.DecimalField(max_digits=6, decimal_places=2, )