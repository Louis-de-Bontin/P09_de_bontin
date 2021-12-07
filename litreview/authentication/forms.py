from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms

User = get_user_model()

class SignupForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ('username', 'email', 'first_name', 'last_name', 'profile_picture')


class UploadProfilePhotoForm(forms.ModelForm):
    # edit_profile_pic = forms.BooleanField(widget=forms.HiddenInput, initial=True)

    class Meta:
        model = get_user_model()
        fields = ('profile_picture', )


# class FollowUserForm(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = ['followed_users']
