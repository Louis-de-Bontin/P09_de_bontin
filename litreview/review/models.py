# from functools import _Descriptor
from django.core.validators import MinValueValidator, MaxValueValidator
from django.conf import settings
from django.db import models
from django.db.models.deletion import CASCADE

class Ticket(models.Model):
    title = models.CharField(max_length=128)
    author = models.CharField(max_length=128)
    description = models.CharField(max_length=128, blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=CASCADE)
    image = models.ImageField(null=True, blank=True)
    time_created = models.DateTimeField(auto_now_add=True)


class Review(models.Model):
    ticket = models.ForeignKey(Ticket, on_delete=CASCADE)

    rating = models.PositiveSmallIntegerField(
        validators=[
            MinValueValidator(0),
            MaxValueValidator(5)]
        )

    headline = models.CharField(max_length=128)
    body = models.CharField(max_length=8192, blank=True)

    user = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=CASCADE
    )
    
    time_created = models.DateTimeField(auto_now_add=True)
