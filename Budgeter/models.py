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

class Expense(models.Model):
    budget = models.ForeignKey(Budget, on_delete=models.CASCADE)
    name = models.CharField(max_length=64)
    amount = models.FloatField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return (reverse('expense', args=[str(self.id)]))

class Purchase(models.Model):
    expense = models.ForeignKey(Expense, on_delete=models.CASCADE)
    name = models.CharField(max_length=64)
    date = models.DateField()
    amount = models.FloatField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return (reverse('purchase', args=[str(self.id)]))
