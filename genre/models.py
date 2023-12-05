from django.db import models

# Create your models here.
class Genre(models.Model):
    genreId = models.AutoField(primary_key=True)
    nameOfGenre = models.CharField(max_length=50)
    description = models.TextField()
   