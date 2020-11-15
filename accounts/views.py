from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordChangeView, PasswordChangeDoneView, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import TemplateView, ListView, DetailView, CreateView, DeleteView, UpdateView

from .models import CustomUser
from .forms import CustomUserCreationForm, CustomUserChangeForm

# Create your views here.
class UserAccount(DetailView):
    template_name = 'accounts/profile.html'
    model = CustomUser


class UpdateAccount(UpdateView):
    template_name = 'accounts/edit_account_personal.html'

    model = CustomUser
    fields = ['first_name', 'last_name', 'email', 'income', 'occupation']

    def get_success_url(self):
        userid = self.kwargs['pk']
        return reverse_lazy('account-view', kwargs={'pk': userid})


class DeleteAccount(DeleteView):
    template_name = 'accounts/delete_account.html'
    success_url = reverse_lazy('home')
    model = CustomUser


class CreateUser(CreateView):
    template_name = "registration/signup.html"
    success_url = reverse_lazy('login')
    form_class = CustomUserCreationForm


class PasswordChange(PasswordChangeView):
    template_name = "registration/password_change_form.html"
    form_class = PasswordChangeForm

    def get_success_url(self):
        userid = self.kwargs['pk']
        return reverse_lazy('pw-change-done', kwargs={'pk': userid})


class PasswordChangeDone(PasswordChangeDoneView):
    template_name = "registration/password_change_done.html"
