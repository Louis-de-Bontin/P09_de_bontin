from django import forms
from django.db.models import fields
from . import models

class TicketForm(forms.ModelForm):
    class Meta:
        model = models.Ticket
        fields = [
            'title',
            'author',
            'description',
            'image'
        ]


class ReviewForm(forms.ModelForm):
    class Meta:
        model = models.Review
        fields = [
            'rating',
            'headline',
            'body'
        ]


class DeleteTicketForm(forms.Form):
    delete_ticket = forms.BooleanField(widget=forms.HiddenInput, initial=True)
