from abc import abstractclassmethod
from typing import AbstractSet
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from PIL import Image

class User(AbstractUser):
    """
    User model, inherit from the django's user model.
    I added the profile picture field and the followed_users, to be able to
    make queries by followed users.
    The method save() is surchared, every time it is called, the size on the image
    is resized.
    """
    profile_picture = models.ImageField(verbose_name='image', null=True, blank=True)
    followed_users = models.ManyToManyField(settings.AUTH_USER_MODEL, through='UserFollow', symmetrical=False)

    IMAGE_MAX_SIZE = (500, 500)
    def resize_image(self):
        profile_picture = Image.open(self.profile_picture)
        profile_picture.thumbnail(self.IMAGE_MAX_SIZE)
        profile_picture.save(self.profile_picture.path)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.resize_image()



class UserFollow(models.Model):
    """
    This model is the representation of the following relationship between users.
    """
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='following'
    )

    followed_user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='followed_by'
    )

    class Meta:
        unique_together=('user', 'followed_user')
