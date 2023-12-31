from django.db import models
from django.core.validators import MinValueValidator

# Create your models here.

# id field is added automatically

# CharFields are shorter than TextFields
# CharFields are meant to be searched for/through, would be too time consuming with longer strings


class Author(models.Model):
    name = models.CharField(max_length=100, blank=False, unique=True)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=100, blank=False, unique=True)
    authors = models.ManyToManyField(Author, related_name="books") 
    pages = models.IntegerField(validators=[MinValueValidator(1)]) # MinVal == 1
    genre = models.CharField(max_length=50, blank=False)
    published_by = models.CharField(max_length=100, blank=False)
    quote = models.CharField(max_length=200, blank=False)

    def __str__(self):
        return self.title


