from django.contrib import admin
from review import models

admin.site.register(models.Ticket)
admin.site.register(models.Review)
