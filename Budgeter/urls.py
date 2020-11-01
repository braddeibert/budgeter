from django.urls import path
from .views import Home, BudgetExpenseList, ExpensePurchaseList, CreateBudget, AddBudgetExpense, AddExpensePurchase
from .views import CreateUser, UserAccount


urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('budgets/<int:pk>', BudgetExpenseList.as_view(), name='budget-detail'),
    path('expense/<int:pk>', ExpensePurchaseList.as_view(), name='expense-detail'),
    path('new_budget/', CreateBudget.as_view(), name='create-budget'),
    path('budgets/<int:pk>/add_expense/', AddBudgetExpense.as_view(), name='add-expense'),
    path('expense/<int:pk>/track_purchase/', AddExpensePurchase.as_view(), name='track-purchase'),
    path('account/<int:pk>', UserAccount.as_view(), name='account-view'),
    path('signup/', CreateUser.as_view(), name='signup')
]