from django.urls import path
from .views import *

urlpatterns = [
    # List views
    path('', Home.as_view(), name='home'),
    path('budgets/<int:pk>', BudgetExpenseList.as_view(), name='budget-detail'),
    path('expense/<int:pk>', ExpensePurchaseList.as_view(), name='expense-detail'),

    # Budget views (CRUD)
    path('new_budget/', CreateBudget.as_view(), name='create-budget'),
    path('budgets/<int:pk>/rename', RenameBudget.as_view(), name='rename-budget'),
    path('budgets/<int:pk>/delete', DeleteBudget.as_view(), name='delete-budget'),

    # Expense views (CRUD)
    path('budgets/<int:pk>/add_expense/', AddBudgetExpense.as_view(), name='add-expense'),
    path('budgets/<int:budget_pk>/edit_expense/<int:pk>', EditBudgetExpense.as_view(), name='edit-expense'),
    path('budgets/<int:budget_pk>/delete_expense/<int:pk>', DeleteBudgetExpense.as_view(), name='delete-expense'),

    # Purchase views
    path('expense/<int:pk>/track_purchase/', AddExpensePurchase.as_view(), name='track-purchase'),
    path('expense/<int:expense_pk>/delete_purchase/<int:pk>', DeleteExpensePurchase.as_view(), name='delete-purchase'),
]