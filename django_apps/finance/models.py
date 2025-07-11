from django.db import models
from django_apps.authentication.models import CustomUser
from utils.models import BaseModelUUID

# Create your models here.
class Balance(BaseModelUUID):
    user = models.ForeignKey(
        CustomUser, 
        on_delete=models.CASCADE
    )
    available_balance = models.DecimalField(
        max_digits=10, 
        decimal_places=2,
        default=0
    )
    
    def __str__(self):
        return f"{self.user.username}'s Balance"
    
    class Meta:
        verbose_name = 'Balance'
        verbose_name_plural = 'Balances'
        ordering = ['user']

class Budget(BaseModelUUID):
    user = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE
    )
    monthly_income = models.DecimalField(
        max_digits=10, 
        decimal_places=2,
        default=0
    )
    monthly_expenses = models.DecimalField(
        max_digits=10, 
        decimal_places=2,
        default=0
    )
    suggested_savings = models.DecimalField(
        max_digits=10, 
        decimal_places=2,
        default=0
    )
    actual_savings = models.DecimalField(
        max_digits=10, 
        decimal_places=2,
        default=0
    )

    def __str__(self):
        return f"{self.user.username}'s Budget"
    
    class Meta:
        verbose_name = 'Budget'
        verbose_name_plural = 'Budgets'
        ordering = ['user']
