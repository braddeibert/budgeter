from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, ListView, DetailView, CreateView, DeleteView, UpdateView

from .models import Budget, Expense, Purchase, User

# Create your views here.
class Home(ListView):
    model = Budget
    template_name = 'home.html'

    # return authenticated user's budgets, or nothing if no user is signed in
    def get_queryset(self):
        try:
            result = Budget.objects.filter(owner=self.request.user)
        except:
            result = None

        return result

class BudgetExpenseList(LoginRequiredMixin, ListView):
    template_name = 'budget.html'

    def get_queryset(self):
        self.budget = get_object_or_404(Budget, id=self.kwargs['pk'])
        return Expense.objects.filter(budget=self.budget)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pk'] = self.budget
        return context


class ExpensePurchaseList(LoginRequiredMixin, ListView):
    template_name = 'expense.html'

    def get_queryset(self):
        self.expense = get_object_or_404(Expense, id=self.kwargs['pk'])
        return Purchase.objects.filter(expense=self.expense)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pk'] = self.expense
        return context


class CreateBudget(CreateView):
    template_name = 'create_budget.html'
    success_url = reverse_lazy('home')

    model = Budget
    fields = ['name', 'owner']


class AddBudgetExpense(CreateView):
    model = Expense
    fields = ['name', 'amount']


class AddExpensePurchase(CreateView):
    model = Purchase
    fields = ['name', 'date', 'amount']


class CreateUser(CreateView):
    template_name = "signup.html"

    model = User
    fields = ['username', 'password']