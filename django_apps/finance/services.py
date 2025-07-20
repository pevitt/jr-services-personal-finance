from django.db.models.base import Model as Model
from django_apps.finance.selectors import BalanceSelector, BudgetSelector
from utils.services.base_service import BaseService
from utils.exceptions import FinanceAPIException, ErrorCode
from typing import List

class BalanceService(BaseService):

    @classmethod
    def create(cls, **kwargs) -> Model:
        balance = BalanceSelector.create(**kwargs)
        return balance
    
    @classmethod
    def get_by_filters(cls, **filters) -> List[Model]:
        return BalanceSelector.get_by_filters(**filters)
    
    @classmethod
    def get_by_id(cls, id: str) -> Model:
        return BalanceSelector.get_by_id(id)
    
    @classmethod
    def update(cls, id: str, **kwargs) -> Model:
        return BalanceSelector.update(id, **kwargs)

class BudgetService(BaseService):

    @classmethod
    def create(cls, **kwargs) -> Model:
        budget = BudgetSelector.create(**kwargs)
        return budget
    
    @classmethod
    def get_by_filters(cls, **filters) -> List[Model]:
        return BudgetSelector.get_by_filters(**filters)
    
    @classmethod
    def get_by_id(cls, id: str) -> Model:
        return BudgetSelector.get_by_id(id)
    
    @classmethod
    def update(cls, id: str, **kwargs) -> Model:
        return BudgetSelector.update(id, **kwargs)

