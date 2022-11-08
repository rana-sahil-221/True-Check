from django.db import models
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class Contact(models.Model):
    email = models.EmailField()
    msg = models.TextField(max_length=255)
    date = models.DateField()

    def __str__(self) -> str:
        return self.email