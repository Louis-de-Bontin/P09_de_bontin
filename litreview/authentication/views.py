from django.http import request
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin
from . import forms
from django.conf import settings

class Signup(View):
    form = forms.SignupForm()
    def get(self, request):
        return render(
            request,
            'authentication/signup.html',
            context={'form': self.form}
        )

    def post(self, request):
        self.form = forms.SignupForm(request.POST)
        print('################')
        print(self.form.is_valid())
        if self.form.is_valid():
            user = self.form.save()
            login(request, user)
            return redirect(settings.LOGIN_REDIRECT_URL)
        else:
            return render(
            request,
            'authentication/signup.html',
            context={'form': self.form}
        )


class PasswordChange(LoginRequiredMixin, View):
    def get(self, request):
        return render(
            request,
            'authentication/password_change.html'
        )

    def post(self, request):
        pass


class FollowUsers(LoginRequiredMixin, View):
    def get(self, request):
        return render(
            request,
            'authentication/follow_users.html'
        )

    def post(self, request):
        pass


class ProfilPicChange(LoginRequiredMixin, View):
    def get(self, request):
        form = forms.UploadProfilePhotoForm(instance=request.user)
        return render(
            request,
            'authentication/profile_pic_change.html',
            {'form': form}
        )

    def post(self, request):
        form = forms.UploadProfilePhotoForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('flux')
        else:
            return render(
                request,
                'authentication/profile_pic_change.html',
                {'form': form}
            )
