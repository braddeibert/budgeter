from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    pass
    income = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    occupation = models.CharField(max_length=64)

    def __str__(self):
        return self.username