from django.conf import settings
from django.shortcuts import (
    render, redirect, get_object_or_404)
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator

from authentication.models import User, UserFollow

from . import forms, models

from itertools import chain


#######################################
#############  Ticket  ################

class TicketCreate(LoginRequiredMixin, View):
    """
    Create a ticket.
    Get the form's data in a POST method, and save it in a new
    instance of a ticket model.
    """
    form = forms.TicketForm()

    def get(self, request):
        return render(
            request,
            'review/ticket_create.html',
            {'form': self.form}
        )

    def post(self, request):
        self.form = forms.TicketForm(request.POST, request.FILES)
        if self.form.is_valid():
            ticket = self.form.save(commit=False)
            ticket.user = request.user
            ticket.save()
            return redirect('flux-self')
        else:
            return render(
                request,
                'review/ticket_create.html',
                {'form': self.form}
            )


class TicketModify(LoginRequiredMixin, View):
    """
    Modify or delete a ticket. Get the id the a GET method.
    If the id deosn't exists, return a 404 error.
    There is 2 different forms, with their own submit button.
    It allows the program to know wich one of them it is, and
    to modify, or delete the ticket.
    """
    def get(self, request, ticket_id):
        self.ticket = get_object_or_404(models.Ticket, id=ticket_id)
        edit_form = forms.TicketForm(instance=self.ticket)
        delete_form = forms.DeleteTicketForm()
        return render(
            request,
            'review/ticket_modify.html',
            context={
                'edit_form': edit_form,
                'delete_form': delete_form
            }
        )

    def post(self, request, ticket_id):
        self.ticket = get_object_or_404(models.Ticket, id=ticket_id)
        if 'edit_ticket' in request.POST:
            edit_form = forms.TicketForm(
                request.POST, request.FILES, instance=self.ticket)
            if edit_form.is_valid():
                edit_form.save()
                return redirect('flux-self')
        if 'delete_ticket' in request.POST:
            delete_form = forms.DeleteTicketForm(request.POST)
            if delete_form.is_valid():
                self.ticket.delete()
                return redirect('flux-self')


class ReviewAndTicketCreate(LoginRequiredMixin, View):
    """
    Create a review without a ticket.
    It will display 2 forms, one for the ticket creation, and one
    for the review.
    The submit button is commun, so both of the instances are created
    at the same time.
    It saves first the ticket, then the review, because the review needs to be
    linked to a ticket.
    """
    ticket_form = forms.TicketForm()
    review_form = forms.ReviewForm()

    def get(self, request):
        return render(
            request,
            'review/ticket_review_create.html',
            context={
                'ticket_form': self.ticket_form,
                'review_form': self.review_form
            }
        )

    def post(self, request):
        self.ticket_form = forms.TicketForm(request.POST, request.FILES)
        self.review_form = forms.ReviewForm(request.POST)
        if self.ticket_form.is_valid() and self.review_form.is_valid():
            ticket = self.ticket_form.save(commit=False)
            ticket.user = request.user
            ticket.save()
            review = self.review_form.save(commit=False)
            review.ticket = ticket
            review.user = request.user
            review.save()
            return redirect('flux-self')
        else:
            return render(
                request,
                'review/ticket_review_create.html',
                context={
                    'ticket_form': self.ticket_form,
                    'review_form': self.review_form
                }
            )

#######################################
##############   Review   #############


class ReviewCreate(LoginRequiredMixin, View):
    """
    Create a review answering to a ticket.
    It gets the ticket id in the GET request.
    If the id doesn't exists, return a 404 error.
    """
    form = forms.ReviewForm()

    def get(self, request, ticket_id):
        self.ticket = get_object_or_404(models.Ticket, id=ticket_id)
        return render(
            request,
            'review/review_create.html',
            context={
                'form': self.form,
                'ticket': self.ticket,
                'hide_button': True
            }
        )

    def post(self, request, ticket_id):
        self.form = forms.ReviewForm(request.POST)
        if self.form.is_valid():
            review = self.form.save(commit=False)
            review.ticket = models.Ticket.objects.get(id=ticket_id)
            review.user = request.user
            review.save()
            return redirect('flux-self')
        else:
            return render(
                request,
                'review/ticket_create.html',
                {'form': self.form}
            )


class ReviewModify(LoginRequiredMixin, View):
    """
    Modify or delete a review. Get the id the a GET method.
    If the id deosn't exists, return a 404 error.
    There is 2 different forms, with their own submit button.
    It allows the program to know wich one of them it is, and
    to modify, or delete the review.
    """
    def get(self, request, review_id):
        self.review = get_object_or_404(models.Review, id=review_id)
        edit_form = forms.ReviewForm(instance=self.review)
        delete_form = forms.DeleteReviewForm()
        return render(
            request,
            'review/review_modify.html',
            context={
                'edit_form': edit_form,
                'delete_form': delete_form,
                'ticket': self.review.ticket
            }
        )

    def post(self, request, review_id):
        self.review = get_object_or_404(models.Review, id=review_id)
        if 'edit_review' in request.POST:
            edit_form = forms.ReviewForm(request.POST, instance=self.review)
            if edit_form.is_valid():
                edit_form.save()
                return redirect('flux-self')
        if 'delete_review' in request.POST:
            delete_form = forms.DeleteReviewForm(request.POST)
            if delete_form.is_valid():
                self.review.delete()
                return redirect('flux-self')

#######################################
##############   FLUX   ###############


def pagination(data, request):
    data = list(data)
    paginator = Paginator(data, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return page_obj


class Flux(LoginRequiredMixin, View):
    """
    Display ALL the tickets and ALL the reviews sorted by date.
    """
    def get(self, request):
        tickets = models.Ticket.objects.all().order_by('-time_created')
        reviews = models.Review.objects.all().order_by('-time_created')
        tickets_and_reviews = sorted(
            chain(tickets, reviews),
            key=lambda instance: instance.time_created,
            reverse=True
        )

        return render(
            request,
            'review/flux.html',
            context={'tickets_and_reviews': pagination(
                tickets_and_reviews, request)}
        )

    def post(self, request):
        pass


class FluxSelf(LoginRequiredMixin, View):
    """
    Display the tickets and the reviews posted by the user logged in.
    """
    def get(self, request):
        tickets = models.Ticket.objects.filter(
            user=request.user).order_by('-time_created')
        reviews = models.Review.objects.filter(
            user=request.user).order_by('-time_created')
        tickets_and_reviews = sorted(
            chain(tickets, reviews),
            key=lambda instance: instance.time_created,
            reverse=True
        )
        message = "Bienvenu sur votre profil " + request.user.username + "."
        return render(
            request,
            'review/flux.html',
            context={
                'tickets_and_reviews': pagination(
                    tickets_and_reviews, request),
                # 'user_profile': request.user,
                'message': message
            }
        )

    def post(self, request):
        pass


class FluxUser(LoginRequiredMixin, View):
    """
    Display the tickets and the review of a particular user.
    His id it passed in a GET request.
    """
    def get(self, request, user_id):
        """
        The first bloc is here to allow the user to follow or unfollow
        the profil of the user he is watching.
        The second bloc is more or less similar to the others Flux views.
        """

        ####################################

        user = get_object_or_404(User, id=user_id)

        if 'follow' in str(request):
            relation = UserFollow()
            relation.user = request.user
            # Set the followed user of the relation by querying it by id
            relation.followed_user = User.objects.get(id=user_id)
            try:
                relation.save()
            except:
                pass
        if 'unfollow' in str(request):
            try:
                # I get the user supposed to be unfollowed
                followed_user = User.objects.get(id=user_id)
                # I get the relation with the user logged in AND
                # the user followed.
                relation = UserFollow.objects.get(
                    user=request.user, followed_user=followed_user
                )
                relation.delete()
            except:
                pass

        ###############################

        tickets = models.Ticket.objects.filter(
            user=user).order_by('-time_created')
        reviews = models.Review.objects.filter(
            user=user).order_by('-time_created')
        tickets_and_reviews = sorted(
            chain(tickets, reviews),
            key=lambda instance: instance.time_created,
            reverse=True
        )
        message = "Bienvenu sur le profile de " + user.username + "."
        relation = UserFollow.objects.filter(
            user=request.user, followed_user=user
        )
        followed = False
        if len(list(relation)) > 0:
            followed = True

        return render(
            request,
            'review/flux.html',
            context={
                'tickets_and_reviews': pagination(
                    tickets_and_reviews, request),
                'user_profile': user,
                'message': message,
                'followed': followed
            }
        )

        ####################################

    def post(self, request):
        pass


class FluxBook(LoginRequiredMixin, View):
    """
    This view displays all the tickets and reviews related to a particular
    book.
    It gets the tickets/reviews by the title and author names.
    I know this code is not clean, but it wasn't in the specifications, so we
    can still get rid of this feature.
    """
    def get(self, request, author_name, book_title):
        tickets = models.Ticket.objects.filter(
            title=book_title, author=author_name
        ).order_by('-time_created')

        tickets_sorted = sorted(
            tickets,
            key=lambda instance: instance.time_created,
            reverse=True
            )
        reviews_sorted = []

        for ticket in tickets:
            reviews = models.Review.objects.filter(
                ticket=ticket
            ).order_by('-time_created')

            reviews_sorted += sorted(
                reviews,
                key=lambda instance: instance.time_created,
                reverse=True
            )

        tickets_and_reviews = sorted(
            chain(reviews_sorted, tickets_sorted),
            key=lambda instance: instance.time_created,
            reverse=True
        )

        return render(
            request,
            'review/flux.html',
            context={'tickets_and_reviews': pagination(
                tickets_and_reviews, request)}
        )

    def post(self, request):
        pass


class FluxTicket(LoginRequiredMixin, View):
    """
    This view displays one ticket and all the reviews related to it.
    """
    def get(self, request, ticket_id):
        print('\n\n\nbonjour\n\n\n')
        ticket = models.Ticket.objects.filter(
            id=ticket_id)
        reviews = models.Review.objects.filter(
            ticket=ticket[0]
        ).order_by('-time_created')

        tickets_and_reviews = chain(ticket, reviews)

        return render(
            request,
            'review/flux.html',
            context={'tickets_and_reviews': tickets_and_reviews}
        )

    def post(self, request, ticket_id):
        print('\n\n\nbonjour\n\n\n')
        pass


class FluxPerso(LoginRequiredMixin, View):
    """
    This view displays a personalised flux for each user.
    It displays tickets and reviews posted by users the logged in user follows,
    his own posts, and the reviews that answer to his tickets.
    """
    def get(self, request):
        # Get the tickets and reviews of the logged in user
        tickets_self = models.Ticket.objects.filter(
            user=request.user).order_by('-time_created')
        reviews_self = models.Review.objects.filter(
            user=request.user).order_by('-time_created')
        tickets_and_reviews = chain(tickets_self, reviews_self)

        # Get the reviews that answer to the tickets posted by
        # the logged in user
        review_answer = []
        for ticket in tickets_self:
            review_answer = models.Review.objects.filter(
                ticket=ticket).order_by('-time_created')
            tickets_and_reviews = chain(review_answer, tickets_and_reviews)

        # Get the data posted by users the logged in user follows
        followed_users = request.user.followed_users.all()
        for user in followed_users:
            tickets_follow = models.Ticket.objects.filter(
                user=user).order_by('-time_created')
            review_follow = models.Review.objects.filter(
                user=user).order_by('-time_created')
            tickets_and_reviews = sorted(
                chain(tickets_and_reviews, tickets_follow, review_follow),
                key=lambda instance: instance.time_created,
                reverse=True
            )

        return render(
            request,
            'review/flux.html',
            context={'tickets_and_reviews': pagination(
                tickets_and_reviews, request)
            }
        )

    def post(self, request):
        pass
