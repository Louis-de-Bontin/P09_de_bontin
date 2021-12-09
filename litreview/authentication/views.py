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
    """
    This view is made for the new profile creation.
    It saves the form's data in a new instance of User, then log him in.
    """
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
    """
    This view is supposed to modify a profile_picture.
    Very similar than the signup view, with only the profile picture thing.
    Note : I pass the user as instance in the form, because I need it to know
    which User to update.
    """
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
    '''
    One of the most complicated view.
    The GET request takes 2 arguments : follow_unfollow and user_id
    When the user arrives on this view, the user_id is supposed to be 0
    If it is, it means that no user hase been selected yet.
    The function get_users() is called without any filter.
    At this point, the user can see the search bar, the users he follows,
    and the users he doesn't follows.
    3 possibilities:
    1) The user click on "subscribe" for a user he doesn't follow yet :
        Send a GET request with follow_unfollow = follow and user_id =
        the id of the user chosen.
        It creates a new relationship (UserFollow instance), with the
        user logged in, and the user chosen.
    2) The user click on "unsubscribe" for a user he follows :
        Does pretty much the same thing but inverted. follow_unfollow =
        unfollow, it gets the users the same way, and delete the relation.
    3) The user write something in the searchbar and press "search" :
        The request method is post, the data is provided with a form.
        Call the function get_user() with a filter a rebuild the querysets.
    '''
    form = forms.SearchUser()

    def get(self, request, follow_unfollow, user_id):
        if user_id != 0:
            if follow_unfollow == 'follow':
                relation = models.UserFollow()
                relation.user = request.user
                # Set the followed user of the relation by querying it by id
                relation.followed_user = models.User.objects.get(id=user_id)
                try:
                    relation.save()
                except:
                    pass
            else:
                try:
                    # I get the user supposed to be unfollowed
                    followed_user = models.User.objects.get(id=user_id)
                    # I get the relation with the user logged in AND
                    # the user followed.
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
        users = self.get_users(request, request.POST['rechercher_un_utilisateur'])
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
        """
        Function that build the queryset.
        If the method is POST, that means that there is a filter, entered by the user
        in an input box. That will filter the query to find the users with a username
        containing the filter.
        It buils 2 queryset, 1 with the followed users and the other with everyone else.
        """
        if filter:
            followed_users = request.user.followed_users.filter(username__contains=filter)
            all_users = models.User.objects.filter(username__contains=filter)
        else:
            followed_users = request.user.followed_users.all()
            all_users = models.User.objects.all()

        not_followed_users = all_users.difference(followed_users)  
        
        return (followed_users, not_followed_users)
