from django.urls import path
from .views import HomeView, BudgetListView, ExpenseListView, PurchaseListView


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('budgets/', BudgetListView.as_view(), name='budget-list'),
]