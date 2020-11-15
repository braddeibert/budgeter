from .models import Budget, Expense, Purchase
from bootstrap_modal_forms.forms import BSModalModelForm

class BudgetForm(BSModalModelForm):
    class Meta:
        model = Budget
        fields = ['name']

class ExpenseForm(BSModalModelForm):
    class Meta:
        model = Expense
        fields = ['name', 'amount']

class PurchaseForm(BSModalModelForm):
    class Meta:
        model = Purchase
        fields = ['name', 'date', 'amount']


