from django.db.models.base import Model as Model
from utils.selectors.base_selector import BaseSelector
from django_apps.transactions.models import Category, Transaction
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
    
    @classmethod
    def update(cls, id: str, **kwargs) -> Model:
        category = cls.get_by_id(id)
        if not category:
            return None
        for key, value in kwargs.items():
            setattr(category, key, value)
        category.save()
        return category
    
    @classmethod
    def exists(cls, **filters) -> bool:
        return cls.model.objects.filter(**filters).exists()
    

class TransactionSelector(BaseSelector):
    model = Transaction

    @classmethod
    def create(cls, **kwargs) -> Transaction:
        return super().create(**kwargs)

    @classmethod
    def get_by_filters(cls, **filters) -> List[Transaction]:
        filters['is_active'] = True
        return cls.model.objects.filter(**filters)

    @classmethod
    def get_by_id(cls, id: str) -> Transaction:
        return cls.model.objects.filter(id=id, is_active=True).first()

    @classmethod
    def update(cls, id: str, **kwargs) -> Transaction:
        transaction = cls.get_by_id(id)
        if not transaction:
            return None
        for key, value in kwargs.items():
            setattr(transaction, key, value)
        transaction.save()
        return transaction

    @classmethod
    def exists(cls, **filters) -> bool:
        filters['is_active'] = True
        return cls.model.objects.filter(**filters).exists()