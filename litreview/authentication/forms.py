from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms

class SignupForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ('username', 'email', 'first_name', 'last_name', 'profile_picture')


class UploadProfilePhotoForm(forms.ModelForm):
    # edit_profile_pic = forms.BooleanField(widget=forms.HiddenInput, initial=True)

    class Meta:
        model = get_user_model()
        fields = ('profile_picture', )
