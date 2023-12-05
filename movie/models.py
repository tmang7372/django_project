from django.db import models

# Create your models here.
class Movie(models.Model):
    movieId = models.AutoField(primary_key=True)
    name = models.TextField()
    description = models.TextField()
    display = models.SmallIntegerField()
    releaseDate = models.DateField()
    imageUrl = models.URLField(blank=True)
    genreId = models.ForeignKey(
        "genre.Genre",
        on_delete = models.CASCADE,
    )
    active = models.CharField(max_length=1)
    dateInserted = models.DateField(auto_now=True)