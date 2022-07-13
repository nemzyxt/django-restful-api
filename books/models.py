from django.db import models

# the Book model
class Book(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=750)

    def __str__(self) -> str:
        return self.title
