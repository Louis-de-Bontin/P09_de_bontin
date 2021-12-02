"""litreview URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin, auth
from django.urls import path

import authentication.views
import review.views
import review_ask.views
import flux.views

urlpatterns = [
    path('admin/', admin.site.urls),
    # Mettre le formulaire de création et de connexion sur la même page
    # Il y aura donc 2 formulaires différents, un qui log l'utilisateur, l'autre qui créé un utilisateur, puis le log
    path('', authentication.views.SignupPage.as_view(), name='signup'),
    path('password-change/', authentication.views.PasswordChange.as_view(), name='password-change'),
    path('follow/', authentication.views.FollowUsers.as_view(), name='follow'),
    path('profil-pic-change/', authentication.views.ProfilPicChange.as_view(), name='profile-pic-change'),

    path('ticket/create/', review_ask.views.TicketCreate.as_view(), name='ticket-create'),
    # Pour modify, il doit récupérer un id en argument et le passer dans l'url
    path('ticket/modify/', review_ask.views.TicketModify.as_view(), name='ticket-modify'),

    path('review/create/answer-to-self/', review.views.ReviewCreateAnswerToSelf.as_view(), name='review-create-self'),
    path('review/create/answer-to-someone/', review.views.ReviewCreateAnswerToSomeone.as_view(), name='review-create-answer'),
    path('review/modify/', review.views.ReviewModify.as_view(), name='review-modify'),

    path('flux/', flux.views.Flux.as_view(), name='flux'),
    path('flux/self/', flux.views.FluxSelf.as_view(), name='flux-self')
]
