from django_apps.transactions.views.views import (
    CategoryView,
    CategoryDetailView,
    TransactionView,
    TransactionDetailView
)
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated

class CategoryJWTView(CategoryView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    pass

class CategoryDetailJWTView(CategoryDetailView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    pass

class TransactionJWTView(TransactionView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    pass

class TransactionDetailJWTView(TransactionDetailView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    pass
