from django import forms
from . import models

class TicketForm(forms.ModelForm):
    """
    Tickets creation and modification form.
    Build with the ticket model.
    """
    edit_ticket = forms.BooleanField(widget=forms.HiddenInput, initial=True)
    class Meta:
        model = models.Ticket
        fields = [
            'title',
            'author',
            'description',
            'image'
        ]


class ReviewForm(forms.ModelForm):
    """
    Review creation and modification form.
    Build with the Review model.
    """
    edit_review = forms.BooleanField(widget=forms.HiddenInput, initial=True)
    class Meta:
        model = models.Review
        fields = [
            'rating',
            'headline',
            'body'
        ]


class DeleteTicketForm(forms.Form):
    """
    Ticket deletion form.
    """
    delete_ticket = forms.BooleanField(widget=forms.HiddenInput, initial=True)


class DeleteReviewForm(forms.Form):
    """
    Ticket deletion form.
    """
    delete_review = forms.BooleanField(widget=forms.HiddenInput, initial=True)
