from django.db.models.base import Model as Model
from django_apps.transactions.selectors import (
    CategorySelector,
    TransactionSelector
)
from utils.services.base_service import BaseService
from utils.exceptions import FinanceAPIException, ErrorCode
from django_apps.transactions.validators.transactions.validator_chain import create_transaction_validation_chain
from typing import List
from django.db import transaction


class CategoryService(BaseService):

    @classmethod
    def create(cls, **kwargs) -> Model:
        if CategorySelector.exists(name=kwargs.get("name")):
            raise FinanceAPIException(error_code=ErrorCode.C01.value)

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
        # Ejecutar la cadena de validación
        validation_chain = create_transaction_validation_chain()
        validation_chain.validate(kwargs)

        with transaction.atomic():
            new_transaction = TransactionSelector.create(**kwargs)
            balance = new_transaction.balance
            category = new_transaction.category

            amount = (
                new_transaction.amount
                if category.type == "income"
                else new_transaction.amount * -1
            )

            balance.available_balance += amount
            balance.save()

            return new_transaction

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
