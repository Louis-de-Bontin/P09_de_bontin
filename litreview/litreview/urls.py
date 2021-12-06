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

from django.contrib.auth.views import LoginView, LogoutView

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    # Mettre le formulaire de création et de connexion sur la même page
    # Il y aura donc 2 formulaires différents, un qui log l'utilisateur, l'autre qui créé un utilisateur, puis le log
    path('', LoginView.as_view(
        template_name='authentication/login.html',
        redirect_authenticated_user = True
    ), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('signup/', authentication.views.Signup.as_view(), name='signup'),
    path('password-change/', authentication.views.PasswordChange.as_view(), name='password-change'),
    path('follow/', authentication.views.FollowUser.as_view(), name='follow'),
    path('profil-pic-change/', authentication.views.ProfilPicChange.as_view(), name='profile-picture-change'),

    path('ticket/create/', review.views.TicketCreate.as_view(), name='ticket-create'),
    path('ticket/modify/<int:ticket_id>', review.views.TicketModify.as_view(), name='ticket-modify'),

    path('review/<int:ticket_id>/create/', review.views.ReviewCreate.as_view(), name='review-create'),
    path('review/modify/<int:review_id>', review.views.ReviewModify.as_view(), name='review-modify'),

    path('review/ticket/create', review.views.ReviewAndTicketCreate.as_view(), name='review-ticket-create'),

    path('flux/', review.views.Flux.as_view(), name='flux'),
    path('flux/self/', review.views.FluxSelf.as_view(), name='flux-self'),
    path('flux/user/<int:user_id>/', review.views.FluxUser.as_view(), name='flux-user'),
    path('flux/user/<str:author_name>/<str:book_title>/', review.views.FluxBook.as_view(), name='flux-book')
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root = settings.MEDIA_ROOT
    )
