from decimal import Decimal
from typing import Any, Dict
from django_apps.finance.selectors import BalanceSelector
from utils.validators.base_validator import BaseValidator
from utils.exceptions import ErrorCode


class BalanceAmountValidationHandler(BaseValidator):
    """
    Validates that balance amount is valid
    """
    
    def _validate(self, data: Dict[str, Any]) -> bool:
        available_balance = data.get('available_balance')
        if available_balance is None:
            self._raise_validation_error(ErrorCode.B00.value)
        
        try:
            balance_decimal = Decimal(str(available_balance))
            if balance_decimal < 0:
                self._raise_validation_error(ErrorCode.B00.value)
            
            # Validar que no sea un monto excesivamente alto
            if balance_decimal > Decimal('1000000000'):  # 1 billón
                self._raise_validation_error(ErrorCode.B00.value)
                
        except (ValueError, TypeError):
            self._raise_validation_error(ErrorCode.B00.value)
        
        return True


class BalanceUserValidationHandler(BaseValidator):
    """
    Validates that user exists and is valid
    """
    
    def _validate(self, data: Dict[str, Any]) -> bool:
        user = data.get('user')
        if not user:
            self._raise_validation_error(ErrorCode.B00.value)
        
        return True


class BalanceExistenceValidationHandler(BaseValidator):
    """
    Validates that balance exists when updating
    """
    
    def _validate(self, data: Dict[str, Any]) -> bool:
        balance_id = data.get('balance_id')
        if not balance_id:
            self._raise_validation_error(ErrorCode.B01.value)
        
        balance = BalanceSelector.get_by_id(balance_id)
        if not balance:
            self._raise_validation_error(ErrorCode.B01.value)
        
        return True 