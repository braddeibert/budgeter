from django.urls import path
from .views import BudgetListView


urlpatterns = [
    path('', BudgetListView.as_view(), name='budget-list'),
]