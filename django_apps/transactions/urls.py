from django.urls import include, path
from django_apps.transactions.views.views import CategoryView

urlpatterns = [
    path(
        'categories/', 
        CategoryView.as_view(), 
        name='category'
    ),
]