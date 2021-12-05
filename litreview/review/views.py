import django
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q

from authentication.models import User
from . import forms, models

from itertools import chain


class ReviewCreate(LoginRequiredMixin, View):
    form = forms.ReviewForm()
    def get(self, request, ticket_id):
        self.ticket = models.Ticket.objects.get(id=ticket_id)
        return render(
            request,
            'review/review_create.html',
            context = {
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
    def get(self, request):
        return render(
            request,
            'review/review_modify.html'
        )

    def post(self, request):
        pass

#######################################
#######################################
#######################################

class Flux(LoginRequiredMixin, View):
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
            context={'tickets_and_reviews': tickets_and_reviews}
        )

    def post(self, request):
        pass


class FluxSelf(LoginRequiredMixin, View):
    def get(self, request):
        tickets = models.Ticket.objects.filter(user=request.user).order_by('-time_created')
        reviews = models.Review.objects.filter(user=request.user).order_by('-time_created')

        tickets_and_reviews = sorted(
            chain(tickets, reviews),
            key=lambda instance: instance.time_created,
            reverse=True
        )

        return render(
            request,
            'review/flux.html',
            context={'tickets_and_reviews': tickets_and_reviews}
        )

    def post(self, request):
        pass

class FluxUser(LoginRequiredMixin, View):
    def get(self, request, user_id):
        user = User.objects.get(id=user_id)
        tickets = models.Ticket.objects.filter(user=user).order_by('-time_created')
        reviews = models.Review.objects.filter(user=user).order_by('-time_created')

        tickets_and_reviews = sorted(
            chain(tickets, reviews),
            key=lambda instance: instance.time_created,
            reverse=True
        )

        return render(
            request,
            'review/flux.html',
            context={'tickets_and_reviews': tickets_and_reviews}
        )

    def post(self, request):
        pass


class FluxBook(LoginRequiredMixin, View):
    def get(self, request, author_name, book_title):
        tickets = models.Ticket.objects.filter(
            Q(title=book_title) & Q(author=author_name)
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

        # print('\n\n\n')
        # print(reviews)
        # print('\n\n\n')

        # tickets_and_reviews = sorted(
        #     chain(tickets, reviews),
        #     key=lambda instance: instance.time_created,
        #     reverse=True
        # )

        print('\n\n\n')
        print(type(tickets_and_reviews))
        print('\n\n\n')

        return render(
            request,
            'review/flux.html',
            context={'tickets_and_reviews': tickets_and_reviews}
        )

    def post(self, request):
        pass

#######################################
#######################################
#######################################

class TicketCreate(LoginRequiredMixin, View):
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
    def get(self, request, ticket_id):
        ticket = get_object_or_404(models.Ticket, id=ticket_id)
        edit_form = forms.TicketForm(instance=ticket)
        delete_form = forms.DeleteTicketForm()
        return render(
            request,
            'review/ticket_modify.html',
            context={
                'edit_form': edit_form,
                'delete_form':delete_form
            }
        )

    def post(self, request, ticket_id):
        pass


# Rajouter une page avec ticket en en-tête avec toutes les reviews dessus et moyenn de note
# Et une où l'on voit les publications d'un profil
