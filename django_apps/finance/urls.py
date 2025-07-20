from django.urls import path
from django_apps.finance.views.views import BalanceView, BalanceDetailView

app_name = 'finance'

urlpatterns = [
    # Balance URLs
    path('balances/', BalanceView.as_view(), name='balance-list'),
    path('balances/<str:balance_id>/', BalanceDetailView.as_view(), name='balance-detail'),
] 