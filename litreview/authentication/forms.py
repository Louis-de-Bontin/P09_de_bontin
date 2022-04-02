from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms


User = get_user_model()


class SignupForm(UserCreationForm):
    """
    This form is used to create a new user.
    It is based on the models.User provided by django.
    I only added the profile picture.
    """
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ('username', 'profile_picture')


class UploadProfilePhotoForm(forms.ModelForm):
    """
    This for is used to update the profile picture.
    Also based on the django's models.User at which I
    added the profile_picture field.
    """
    class Meta:
        model = get_user_model()
        fields = ('profile_picture', )


class SearchUser(forms.Form):
    """
    Basic input searchbar to easely look for a user which
    username contains the input.
    """
    rechercher_un_utilisateur = forms.CharField(max_length=50, required=False)
