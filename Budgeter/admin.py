from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from .models import Budget, Expense, Purchase, Budgeter

class BudgeterInline(admin.StackedInline):
    model = Budgeter
    can_delete = False
    verbose_name_plural = 'Budgeter Info'

class UserAdmin(BaseUserAdmin):
    inlines = (BudgeterInline,)

# Register your models here.
admin.site.register(Budget)
admin.site.register(Expense)
admin.site.register(Purchase)
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
