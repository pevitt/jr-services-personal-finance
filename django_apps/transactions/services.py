from django.db.models.base import Model as Model
from django_apps.transactions.selectors import CategorySelector
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
