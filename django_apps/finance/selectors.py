from django.db.models.base import Model as Model
from utils.selectors.base_selector import BaseSelector
from django_apps.finance.models import Balance, Budget
from typing import List

class BalanceSelector(BaseSelector):
    model = Balance

    @classmethod
    def create(cls, **kwargs) -> Model:
        return super().create(**kwargs)

    @classmethod
    def get_by_filters(cls, **filters) -> List[Model]:
        return cls.model.objects.filter(**filters)
    
    @classmethod
    def get_by_id(cls, id: str) -> Model:
        return cls.model.objects.filter(id=id).first()
    
    @classmethod
    def update(cls, id: str, **kwargs) -> Model:
        balance = cls.get_by_id(id)
        if not balance:
            return None
        for key, value in kwargs.items():
            setattr(balance, key, value)
        balance.save()
        return balance
    
    @classmethod
    def exists(cls, **filters) -> bool:
        return cls.model.objects.filter(**filters).exists()

class BudgetSelector(BaseSelector):
    model = Budget

    @classmethod
    def create(cls, **kwargs) -> Model:
        return super().create(**kwargs)

    @classmethod
    def get_by_filters(cls, **filters) -> List[Model]:
        return cls.model.objects.filter(**filters)
    
    @classmethod
    def get_by_id(cls, id: str) -> Model:
        return cls.model.objects.filter(id=id).first()
    
    @classmethod
    def update(cls, id: str, **kwargs) -> Model:
        budget = cls.get_by_id(id)
        if not budget:
            return None
        for key, value in kwargs.items():
            setattr(budget, key, value)
        budget.save()
        return budget
    
    @classmethod
    def exists(cls, **filters) -> bool:
        return cls.model.objects.filter(**filters).exists()
