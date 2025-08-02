from django.urls import include, path
from django_apps.transactions.views.api_views import (
    CategoryAPIView,
    CategoryDetailAPIView,
    TransactionAPIView,
    TransactionDetailAPIView
)

from django_apps.transactions.views.jwt_views import (
    CategoryJWTView,
    CategoryDetailJWTView,
    TransactionJWTView,
    TransactionDetailJWTView
)

urlpatterns = [
    path(
        'categories/', 
        CategoryAPIView.as_view(), 
        name='category'
    ),
    path(
        'categories/<str:category_id>/',
        CategoryDetailAPIView.as_view(),
        name='category-detail'
    ),
    path(
        'transactions/',
        TransactionAPIView.as_view(),
        name='transaction'
    ),
    path(
        'transactions/<str:transaction_id>/',
        TransactionDetailAPIView.as_view(),
        name='transaction-detail'
    ),
]

urlpatterns_jwt = [
    path(
        'categories/',
        CategoryJWTView.as_view(),
        name='category'
    ),
    path(
        'categories/<str:category_id>/',
        CategoryDetailJWTView.as_view(),
        name='category-detail'
    ),
    path(
        'transactions/',
        TransactionJWTView.as_view(),
        name='transaction'
    ),
    path(
        'transactions/<str:transaction_id>/',
        TransactionDetailJWTView.as_view(),
        name='transaction-detail'
    ),
]