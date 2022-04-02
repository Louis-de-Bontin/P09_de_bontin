# Generated by Django 3.2.9 on 2021-12-09 07:58

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='followed_users',
            field=models.ManyToManyField(through='authentication.UserFollow', to=settings.AUTH_USER_MODEL),
        ),
    ]
