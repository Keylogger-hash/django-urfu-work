from django.db import models

# Create your models here.
class Genre(models.Model):
    name = models.CharField(max_length=255)


class Author(models.Model):
    fio = models.CharField(max_length=255)


class Book(models.Model):
    title = models.CharField(max_length=255)
    authors = models.ManyToManyField(Author)
    city = models.CharField(max_length=255)
    genre = models.ManyToManyField(Genre)
    year = models.DateField()
    pages_count = models.IntegerField()

    def __str__(self):
        return f"{self.title}"
