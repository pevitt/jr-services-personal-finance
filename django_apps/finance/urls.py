from django.urls import path
from django_apps.finance.views.api_views import (
    BalanceAPIView, 
    BalanceDetailAPIView, 
    BudgetAPIView, 
    BudgetDetailAPIView
)
from django_apps.finance.views.jwt_views import (
    BalanceJWTView, 
    BalanceDetailJWTView, 
    BudgetJWTView, 
    BudgetDetailJWTView
)

app_name = 'finance'

urlpatterns = [
    # Balance URLs
    path('balances/', BalanceAPIView.as_view(), name='balance-list'),
    path('balances/<str:balance_id>/', BalanceDetailAPIView.as_view(), name='balance-detail'),
    
    # Budget URLs
    path('budgets/', BudgetAPIView.as_view(), name='budget-list'),
    path('budgets/<uuid:budget_id>/', BudgetDetailAPIView.as_view(), name='budget-detail'),
] 

urlpatterns_jwt = [
    # Balance URLs
    path('balances/', BalanceJWTView.as_view(), name='balance-list'),
    path('balances/<str:balance_id>/', BalanceDetailJWTView.as_view(), name='balance-detail'),
    
    # Budget URLs
    path('budgets/', BudgetJWTView.as_view(), name='budget-list'),
    path('budgets/<uuid:budget_id>/', BudgetDetailJWTView.as_view(), name='budget-detail'),
]