from django.db.models.base import Model as Model
from django_apps.finance.selectors import BalanceSelector, BudgetSelector
from utils.services.base_service import BaseService
from utils.exceptions import FinanceAPIException, ErrorCode
from typing import List
from utils.strategies.savings_strategies import SavingsStrategyFactory
from typing import Dict

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
        if BudgetSelector.exists(user=kwargs.get('user')):
            raise FinanceAPIException(
                error_code=ErrorCode.B01.value
            )
        
        budget = BudgetSelector.create(**kwargs)
        return budget
    
    @classmethod
    def get_by_filters(cls, **filters) -> List[Model]:
        return BudgetSelector.get_by_filters(**filters)
    
    @classmethod
    def get_by_id(cls, id: str, strategy: str = 'balanced') -> Dict:
        budget = BudgetSelector.get_by_id(id)
        strategy = SavingsStrategyFactory.create_strategy(strategy)
        suggested_savings = strategy.calculate_suggested_savings(budget.monthly_income)

        return {
            'id': budget.id,
            'user': budget.user,
            'monthly_income': budget.monthly_income,
            'monthly_expenses': budget.monthly_expenses,
            'suggested_savings': suggested_savings,
            'actual_savings': budget.actual_savings,
            'created_at': budget.created_at,
            'updated_at': budget.updated_at,
            'strategy_used': strategy.get_strategy_name(),
            'strategy_description': strategy.get_strategy_description()
        }
    
    @classmethod
    def update(cls, id: str, **kwargs) -> Model:
        return BudgetSelector.update(id, **kwargs)

