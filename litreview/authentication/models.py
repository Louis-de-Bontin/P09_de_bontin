from abc import abstractclassmethod
from typing import AbstractSet
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

class User(AbstractUser):
    profile_picture = models.ImageField(verbose_name='image', null=True, blank=True)
    follows = models.ManyToManyField(
        'self',
        # through='UserFollows'
        symmetrical=False,
        verbose_name='suit'
    )


class UserFollows(AbstractSet):

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
