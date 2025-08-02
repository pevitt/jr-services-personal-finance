from django_apps.transactions.views.views import (
    CategoryView,
    CategoryDetailView,
    TransactionView,
    TransactionDetailView
)
from utils.api_key_auth import HasValidAPIKey

class CategoryAPIView(CategoryView):
    authentication_classes = []
    permission_classes = [HasValidAPIKey]
    pass

class CategoryDetailAPIView(CategoryDetailView):
    authentication_classes = []
    permission_classes = [HasValidAPIKey]
    pass

class TransactionAPIView(TransactionView): 
    authentication_classes = []
    permission_classes = [HasValidAPIKey]
    pass

class TransactionDetailAPIView(TransactionDetailView):
    authentication_classes = []
    permission_classes = [HasValidAPIKey]
    pass
