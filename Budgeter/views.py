from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views.generic import TemplateView, ListView, DetailView

from .models import Budget, Expense, Purchase

# Create your views here.
class HomeView(ListView):
    model = Budget 

    template_name = 'home.html'

class BudgetListView(ListView):
    model = Budget
    
    template_name = 'budget.html'


class ExpenseListView(ListView):
    model = Expense

    template_name = 'expense.html'


class PurchaseListView(ListView):
    model = Purchase

    template_name = 'purchase.html'


