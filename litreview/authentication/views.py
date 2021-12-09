from django.contrib import auth
from django.contrib.auth.models import User
from django.http import request
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin
from . import forms, models
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
        self.form = forms.SignupForm(request.POST, request.FILES)
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


class FollowUser(LoginRequiredMixin, View):
    form = forms.SearchUser()

    def get(self, request, follow_unfollow, user_id):
        if user_id != 0:
            if type == 'follow':
                relation = models.UserFollow()
                relation.user = request.user
                relation.followed_user = models.User.objects.get(id=user_id)
                try:
                    relation.save()
                except:
                    pass
            else:
                try:
                    followed_user = models.User.objects.get(id=user_id)
                    relation = models.UserFollow.objects.get(
                        user = request.user, followed_user=followed_user
                    )
                    relation.delete()
                except:
                    pass
        
        users = self.get_users(request)

        return render(
            request,
            'authentication/follow_users.html',
            context={
                'followed_users': users[0],
                'not_followed_users': users[1],
                'form': self.form
            }
        )

    def post(self, request, follow_unfollow, user_id):
        self.form = forms.SearchUser(request.POST)

        users = self.get_users(request, request.POST['rechercher_un_utilisateur'].upper())
        # print(users)

        # for user_grp in users:
        #     print(user_grp)
        #     for user in user_grp:
        #         print(user)
        #         print('Recherche :' , request.POST['rechercher_un_utilisateur'].upper())
        #         print('Comparé à : ', user.username.upper())
        #         if request.POST['rechercher_un_utilisateur'].upper() not in user.username.upper():
        #             user_grp.remove(user)
        
        # print(users)

        return render(
            request,
            'authentication/follow_users.html',
            context={
                'followed_users': users[0],
                'not_followed_users': users[1],
                'form': self.form
            }
        )

    
    def get_users(self, request, filter=None):
        # relations = list(models.UserFollow.objects.filter(
        #     user=request.user)
        # )

        # if filter:
        #     print(filter)
        #     "je veux les amis dont le pseudo contienne le filtre"
        #     "je veux les non amis dont le pseudo contien le filtre"
        # else:
        #     print(filter)
        #     followed_users = models.User.objects.filter(
        #         username=relations.
        #     )
        #     print('\n\n\n')
        #     print(followed_users)
        #     print('\n\n\n')
        #     not_followed_users = []



        relations = list(models.UserFollow.objects.filter(
            user=request.user)
        )

        not_followed_users = list(models.User.objects.all())

        followed_users = []
        for relation in relations:
            user_followed = relation.followed_user
            not_followed_users.remove(relation.followed_user)
            followed_users.append(user_followed)
        
        if request.user in followed_users:
            followed_users.remove(request.user)
        elif request.user in not_followed_users:
            not_followed_users.remove(request.user)
        
        return (followed_users, not_followed_users)
