from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.contrib.auth.models import User
from .forms import UserForm


class HomeView(CreateView, ListView):
    model = User
    form_class = UserForm
    template_name = "home/index.html"
    success_url = "/"

    def get_queryset(self) -> QuerySet[Any]:
        return super().get_queryset().exclude(is_superuser=True)


class UserUpdateView(UpdateView):
    model = User
    form_class = UserForm
    template_name = "home/update.html"
    success_url = "/"


class UserDeleteView(DeleteView):
    model = User
    template_name = "home/delete.html"
    success_url = "/"
