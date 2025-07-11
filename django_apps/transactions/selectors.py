from django.db.models.base import Model as Model
from utils.selectors.base_selector import BaseSelector
from django_apps.transactions.models import Category

class CategorySelector(BaseSelector):
    model = Category

    @classmethod
    def create(cls, **kwargs) -> Model:
        return super().create(**kwargs)

    @classmethod
    def get_category_by_name(cls, name: str) -> Category:
        return cls.model.objects.filter(name=name).first()