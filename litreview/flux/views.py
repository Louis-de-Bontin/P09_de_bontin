from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin


class Flux(View): # add mixin after
    def get(self, request):
        return render(
            request,
            'flux/flux.html'
        )

    def post(self, request):
        pass


class FluxSelf(View): # add mixin after
    def get(self, request):
        return render(
            request,
            'flux/flux_self.html'
        )

    def post(self, request):
        pass
