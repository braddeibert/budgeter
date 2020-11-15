from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordChangeView, PasswordChangeDoneView, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import TemplateView, ListView, DetailView, CreateView, DeleteView, UpdateView

from bootstrap_modal_forms.generic import BSModalCreateView, BSModalUpdateView, BSModalDeleteView, BSModalReadView

from .models import *
from .forms import *

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


class BudgetExpenseList(LoginRequiredMixin, UserPassesTestMixin, ListView):
    template_name = 'budget.html'

    def test_func(self):
        return self.request.user == Budget.objects.get(pk=self.kwargs['pk']).owner

    def get_queryset(self):
        self.budget = get_object_or_404(Budget, id=self.kwargs['pk'])
        return Expense.objects.filter(budget=self.budget)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pk'] = self.budget
        return context


class ExpensePurchaseList(LoginRequiredMixin, UserPassesTestMixin, ListView):
    template_name = 'expense.html'

    def test_func(self):
        return self.request.user == Expense.objects.get(pk=self.kwargs['pk']).budget.owner

    def get_queryset(self):
        self.expense = get_object_or_404(Expense, id=self.kwargs['pk'])
        return Purchase.objects.filter(expense=self.expense)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pk'] = self.expense
        return context


class CreateBudget(BSModalCreateView):
    template_name = 'create_budget.html'
    form_class = BudgetForm
    success_url = reverse_lazy('home')
    success_message = 'Budget created successfully.'

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)
        

class RenameBudget(BSModalUpdateView):
    model = Budget
    template_name = 'edit_budget.html'
    form_class = BudgetForm
    success_message = 'Budget renamed successfully.'

    def get_success_url(self):
        budgetid = self.kwargs['pk']
        return reverse_lazy('budget-detail', kwargs={'pk': budgetid})


class DeleteBudget(DeleteView):
    template_name = 'delete_budget.html'
    success_url = reverse_lazy('home')
    model = Budget


class AddBudgetExpense(BSModalCreateView):
    template_name = 'add_expense.html'
    form_class = ExpenseForm
    success_message = 'Expense added successfully.'

    def get_success_url(self):
        budgetid = self.kwargs['pk']
        return reverse_lazy('budget-detail', kwargs={'pk': budgetid})

    def form_valid(self, form):
        form.instance.budget = Budget.objects.get(pk=self.kwargs['pk'])
        return super().form_valid(form)


class EditBudgetExpense(BSModalUpdateView):
    model = Expense
    template_name = 'edit_expense.html'
    form_class = ExpenseForm
    success_message = 'Edits saved successfully.'

    def get_success_url(self):
        budgetid = self.kwargs['budget_pk']
        return reverse_lazy('budget-detail', kwargs={'pk': budgetid})


class DeleteBudgetExpense(BSModalDeleteView):
    model = Expense
    template_name = 'delete_expense.html'
    form_class = ExpenseForm
    success_message = 'Expense deleted successfully.'

    def get_success_url(self):
        budgetid = self.kwargs['budget_pk']
        return reverse_lazy('budget-detail', kwargs={'pk': budgetid})


class AddExpensePurchase(BSModalCreateView):
    template_name = 'track_purchase.html'
    form_class = PurchaseForm
    success_message = 'Purchase added successfully.'

    def get_success_url(self):
        expenseid = self.kwargs['pk']
        return reverse_lazy('expense-detail', kwargs={'pk': expenseid})

    def form_valid(self, form):
        form.instance.expense = Expense.objects.get(pk=self.kwargs['pk'])
        return super().form_valid(form)


class DeleteExpensePurchase(BSModalDeleteView):
    model = Purchase
    template_name = 'delete_purchase.html'
    form_class = PurchaseForm
    success_message = 'Purchase deleted successfully.'

    def get_success_url(self):
        expenseid = self.kwargs['expense_pk']
        return reverse_lazy('expense-detail', kwargs={'pk': expenseid})

        
class UserAccount(DetailView):
    template_name = 'accounts/profile.html'
    model = User


class UpdateAccount(UpdateView):
    template_name = 'accounts/edit_account_personal.html'

    model = User
    fields = ['first_name', 'last_name', 'email']

    def get_success_url(self):
        userid = self.kwargs['pk']
        return reverse_lazy('account-view', kwargs={'pk': userid})


class DeleteAccount(DeleteView):
    template_name = 'accounts/delete_account.html'
    success_url = reverse_lazy('home')
    model = User


class CreateUser(CreateView):
    template_name = "registration/signup.html"
    success_url = reverse_lazy('login')
    form_class = UserCreationForm


class PasswordChange(PasswordChangeView):
    template_name = "registration/password_change_form.html"
    form_class = PasswordChangeForm

    def get_success_url(self):
        userid = self.kwargs['pk']
        return reverse_lazy('pw-change-done', kwargs={'pk': userid})


class PasswordChangeDone(PasswordChangeDoneView):
    template_name = "registration/password_change_done.html"


#class DeletePurchase(DeleteView):
