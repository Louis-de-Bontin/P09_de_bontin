# from functools import _Descriptor
from django.core.validators import MinValueValidator, MaxValueValidator
from django.conf import settings
from django.db import models
from django.db.models.deletion import CASCADE
from PIL import Image


class Ticket(models.Model):
    """
    Tcket model.
    It is linked to his creator by a OneToMany relation. One ticket
    can have only one creator.
    The save() method is surcharged to resize the book image, and to
    store the title and author name in capital.
    """
    title = models.CharField(max_length=128)
    author = models.CharField(max_length=128)
    description = models.TextField(max_length=1024, blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=CASCADE)
    image = models.ImageField(null=True, blank=True)
    time_created = models.DateTimeField(auto_now_add=True)

    IMAGE_MAX_SIZE = (300, 500)

    def resize_image(self):
        image = Image.open(self.image)
        image.thumbnail(self.IMAGE_MAX_SIZE)
        image.save(self.image.path)

    def save(self, *args, **kwargs):
        self.author = self.author.upper()
        self.title = self.title.upper()
        super().save(*args, **kwargs)
        try:
            self.resize_image()
        except:
            pass


class Review(models.Model):
    """
    Review model.
    Same as ticket, it is linked to it's creator by a OneToMany relation.
    But it is also linked to a ticket, the same way, because a review is
    an answer to a ticket. Inded, the creation of a review alone will
    create an assotiated ticket.
    """
    ticket = models.ForeignKey(Ticket, on_delete=CASCADE)
    rating = models.PositiveSmallIntegerField(
        validators=[
            MinValueValidator(0),
            MaxValueValidator(5)]
        )
    headline = models.CharField(max_length=128)
    body = models.TextField(max_length=8192, blank=True)
    user = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=CASCADE
    )
    time_created = models.DateTimeField(auto_now_add=True)
