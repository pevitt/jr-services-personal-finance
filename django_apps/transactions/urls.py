from django.urls import include, path
from django_apps.transactions.views.views import CategoryView, CategoryDetailView

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
]