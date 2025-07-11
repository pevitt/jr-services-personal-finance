from django.db import models
from utils.models import BaseModelUUID
from django_apps.finance.models import Balance

# Create your models here.
class Category(BaseModelUUID):
    CATEGORY_TYPE = (
        ('income', 'Income'),
        ('expenses', 'Expenses'),
    )
    name = models.CharField(
        max_length=255
    )
    type = models.CharField(
        max_length=10, 
        choices=CATEGORY_TYPE
    )
    description = models.TextField(
        blank=True, 
        null=True
    )

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ['name']
        unique_together = ('name', 'type')


class Transaction(BaseModelUUID):
    balance = models.ForeignKey(
        Balance,
        on_delete=models.CASCADE,
        related_name='transactions'
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE
    )
    amount = models.DecimalField(
        max_digits=10, 
        decimal_places=2,
        default=0
    )
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.balance.user.username}'s Transaction"
    
    class Meta:
        verbose_name = 'Transaction'
        verbose_name_plural = 'Transactions'
        ordering = ['balance']
        indexes = [
            models.Index(fields=['balance', 'category', 'amount'])
        ]
 