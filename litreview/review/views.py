from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin


class ReviewCreateAnswerToSelf(View): # add mixin after
    def get(self, request):
        return render(
            request,
            'review/review_create_self.html'
        )

    def post(self, request):
        pass


class ReviewCreateAnswerToSomeone(View): # add mixin after
    def get(self, request):
        return render(
            request,
            'review/review_create_answer.html'
        )

    def post(self, request):
        pass


class ReviewModify(View): # add mixin after
    def get(self, request):
        return render(
            request,
            'review/review_modify.html'
        )

    def post(self, request):
        pass