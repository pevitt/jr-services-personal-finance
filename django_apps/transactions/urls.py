from django.urls import include, path
from django_apps.transactions.views.views import (
    CategoryView, 
    CategoryDetailView, 
    TransactionView, 
    TransactionDetailView
)

urlpatterns = [
    path(
        'categories/', 
        CategoryView.as_view(), 
        name='category'
    ),
    path(
        'categories/<str:category_id>/',
        CategoryDetailView.as_view(),
        name='category-detail'
    ),
    path(
        'transactions/',
        TransactionView.as_view(),
        name='transaction'
    ),
    path(
        'transactions/<str:transaction_id>/',
        TransactionDetailView.as_view(),
        name='transaction-detail'
    ),
]