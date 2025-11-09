from django.db import models


class Book(models.Model):
    """Represents a single book entry stored in the library catalogue."""

    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField()

    def __str__(self) -> str:
        return f"{self.title} by {self.author} ({self.publication_year})"
