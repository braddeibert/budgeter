from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.
class Budget(models.Model):
    name = models.CharField(max_length=64)
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return (reverse('budget', args=[str(self.id)]))   

    def get_total_expenses(self):
        self.expenses = Expense.objects.filter(budget=self.id)
        self.total_expenses = 0

        for expense in self.expenses:
            self.total_expenses += expense.amount

        return self.total_expenses

    def get_remaining_funds(self):
        self.expenses = Expense.objects.filter(budget=self.id)
        budgeted = self.get_total_expenses()
        spent = 0

        for expense in self.expenses:
            spent += expense.get_purchases()[1]

        self.remaining_funds = budgeted - spent

        return self.remaining_funds

    def get_number_expenses(self):
        self.expenses = Expense.objects.filter(budget=self.id)
        return len(self.expenses)

    def get_number_purchases(self):
        self.expenses = Expense.objects.filter(budget=self.id)
        num_purchases = 0

        for expense in self.expenses:
            num_purchases += expense.get_purchases()[0]

        return num_purchases


class Expense(models.Model):
    budget = models.ForeignKey(Budget, on_delete=models.CASCADE)
    name = models.CharField(max_length=64)
    amount = models.FloatField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return (reverse('expense', args=[str(self.id)]))

    def get_purchases(self):
        self.purchases = Purchase.objects.filter(expense=self.id)
        self.total = 0
        self.num_purchases = 0

        for purchase in self.purchases:
            self.total += purchase.amount
            self.num_purchases += 1

        return self.num_purchases, self.total

    def net(self):
        return self.amount - self.get_purchases()[1]


class Purchase(models.Model):
    expense = models.ForeignKey(Expense, on_delete=models.CASCADE)
    name = models.CharField(max_length=64)
    date = models.DateField()
    amount = models.FloatField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return (reverse('purchase', args=[str(self.id)]))


class Budgeter(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    income = models.FloatField()
    
