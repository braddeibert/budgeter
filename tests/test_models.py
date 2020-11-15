from django.test import TestCase
from django.contrib.auth.models import User
import datetime

from Budgeter.models import Budget, Expense, Purchase

# Model tests
class ModelTests(TestCase):
    def setUp(self):
        User.objects.create(username='testuser')
        testuser = User.objects.get(username='testuser')

        Budget.objects.create(name='fruits', owner=testuser)
        testbudget = Budget.objects.get(name='fruits')

        Expense.objects.create(name='apple', amount='2.00', budget=testbudget)
        Expense.objects.create(name='oranges', amount='5.00', budget=testbudget)
        Expense.objects.create(name='bananas', amount='100.00', budget=testbudget)
        testexpense = Expense.objects.get(name='bananas')

        Purchase.objects.create(name='one nanner', date='2000-1-1', amount='1.00', expense=testexpense)
        Purchase.objects.create(name='fifty nanners', date='2005-1-1', amount='50.00', expense=testexpense)


    def test_budget(self):
        budget = Budget.objects.get(name='fruits')

        self.assertEqual(budget.owner.username, 'testuser')

        self.assertEqual(str(budget), 'fruits')
        self.assertEqual(budget.get_total_expenses(), 107)
        self.assertEqual(budget.get_remaining_funds(), 56)
        self.assertEqual(budget.get_number_expenses(), 3)
        self.assertEqual(budget.get_number_purchases(), 2)


    def test_expense(self):
        expense = Expense.objects.get(name='bananas')

        self.assertEqual(expense.budget.name, 'fruits')
        self.assertEqual(expense.amount, 100)

        self.assertEqual(str(expense), 'bananas')
        self.assertEqual(expense.get_purchases()[0], 2)
        self.assertEqual(expense.get_purchases()[1], 51)
        self.assertEqual(expense.net(), 49)


    def test_purchase(self):
        purchase = Purchase.objects.get(name='fifty nanners')

        self.assertEqual(purchase.expense.budget.name, 'fruits')
        self.assertEqual(purchase.expense.name, 'bananas')
        self.assertEqual(purchase.date, datetime.date(2005, 1, 1))
        self.assertEqual(purchase.amount, 50)

        self.assertEqual(str(purchase), 'fifty nanners')


