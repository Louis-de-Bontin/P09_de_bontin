from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin


class SignupPage(View):
    def get(self, request):
        return render(
            request,
            'authentication/signup.html'
        )

    def post(self, request):
        pass


class PasswordChange(View): # add mixin after
    def get(self, request):
        return render(
            request,
            'authentication/password_change.html'
        )

    def post(self, request):
        pass


class FollowUsers(View): # add mixin after
    def get(self, request):
        return render(
            request,
            'authentication/follow_users.html'
        )

    def post(self, request):
        pass


class ProfilPicChange(View): # add mixin after
    def get(self, request):
        return render(
            request,
            'authentication/profile_pic_change.html'
        )

    def post(self, request):
        pass