from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView, ListView

from .models import Budget, Expense, Purchase

# Create your views here.
class BudgetListView(ListView):
    model = Budget
    
    template_name = 'budget.html'

class ExpenseView(TemplateView):
    template_name = 'expense.html'

class PurchaseView(TemplateView):
    template_name = 'purchase.html'