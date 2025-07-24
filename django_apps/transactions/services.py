from django.db.models.base import Model as Model
from django_apps.transactions.selectors import CategorySelector, TransactionSelector
from utils.services.base_service import BaseService
from utils.exceptions import FinanceAPIException, ErrorCode
from typing import List

class CategoryService(BaseService):

    @classmethod
    def create(cls, **kwargs) -> Model:
        if CategorySelector.exists(name=kwargs.get('name')):
            raise FinanceAPIException(
                error_code=ErrorCode.C01.value
            )
        
        category = CategorySelector.create(**kwargs)

        return category
    
    @classmethod
    def get_by_filters(cls, **filters) -> List[Model]:
        return CategorySelector.get_by_filters(**filters)
    
    @classmethod
    def get_by_id(cls, id: str) -> Model:
        return CategorySelector.get_by_id(id)
    
    @classmethod
    def update(cls, id: str, **kwargs) -> Model:
        return CategorySelector.update(id, **kwargs)


class TransactionService(BaseService):

    @classmethod
    def create(cls, **kwargs):
        return TransactionSelector.create(**kwargs)

    @classmethod
    def get_by_filters(cls, **filters):
        return TransactionSelector.get_by_filters(**filters)

    @classmethod
    def get_by_id(cls, id):
        return TransactionSelector.get_by_id(id)

    @classmethod
    def update(cls, id, **kwargs):
        return TransactionSelector.update(id, **kwargs)

    @classmethod
    def exists(cls, **filters):
        return TransactionSelector.exists(**filters)