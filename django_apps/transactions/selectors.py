from django.db.models.base import Model as Model
from utils.selectors.base_selector import BaseSelector
from django_apps.transactions.models import Category
from typing import List

class CategorySelector(BaseSelector):
    model = Category

    @classmethod
    def create(cls, **kwargs) -> Model:
        return super().create(**kwargs)

    @classmethod
    def get_category_by_name(cls, name: str) -> Category:
        return cls.model.objects.filter(name=name).first()
    
    @classmethod
    def get_by_filters(cls, **filters) -> List[Model]:
        return cls.model.objects.filter(**filters)
    
    @classmethod
    def get_by_id(cls, id: str) -> Model:
        return cls.model.objects.filter(id=id).first()