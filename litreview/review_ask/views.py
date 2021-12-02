from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin


class TicketCreate(View): # add mixin after
    def get(self, request):
        return render(
            request,
            'review_ask/ticket_create.html'
        )

    def post(self, request):
        pass


class TicketModify(View): # add mixin after
    def get(self, request):
        return render(
            request,
            'review_ask/ticket_modify.html'
        )

    def post(self, request):
        pass
