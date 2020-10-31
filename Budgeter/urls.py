from django.urls import path
from .views import Home, BudgetExpenseList, ExpensePurchaseList, CreateBudget, CreateUser


urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('budgets/<int:pk>', BudgetExpenseList.as_view(), name='budget-detail'),
    path('expense/<int:pk>', ExpensePurchaseList.as_view(), name='expense-detail'),
    path('new_budget/', CreateBudget.as_view(), name='create-budget'),
    path('signup/', CreateUser.as_view(), name='signup')
]