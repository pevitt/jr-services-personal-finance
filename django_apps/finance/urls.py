from django.urls import path
from django_apps.finance.views.views import (
    BalanceView, 
    BalanceDetailView, 
    BudgetView, 
    BudgetDetailView
)

app_name = 'finance'

urlpatterns = [
    # Balance URLs
    path('balances/', BalanceView.as_view(), name='balance-list'),
    path('balances/<str:balance_id>/', BalanceDetailView.as_view(), name='balance-detail'),
    
    # Budget URLs
    path('budgets/', BudgetView.as_view(), name='budget-list'),
    path('budgets/<uuid:budget_id>/', BudgetDetailView.as_view(), name='budget-detail'),
] 