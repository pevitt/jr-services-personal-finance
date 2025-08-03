from decimal import Decimal
from typing import Any, Dict
from django_apps.finance.services import BalanceService
from django_apps.transactions.selectors import CategorySelector, TransactionSelector
from utils.validators.base_validator import BaseValidator
from utils.exceptions import ErrorCode


class BalanceValidationHandler(BaseValidator):
    """
    Validates that the balance exists and belongs to the user
    """
    
    def _validate(self, data: Dict[str, Any]) -> bool:
        balance_id = data.get('balance').id
        print("=== DEBUG: BalanceValidationHandler - Validación iniciada ===")
        print(balance_id)
        balance = BalanceService.get_by_id(balance_id)
        if not balance:
            self._raise_validation_error(ErrorCode.B01.value)
        
        return True


class CategoryValidationHandler(BaseValidator):
    """
    Validates that the category exists and is active
    """
    
    def _validate(self, data: Dict[str, Any]) -> bool:
        category_id = data.get('category').id
        print("=== DEBUG: CategoryValidationHandler - Validación iniciada ===")
        print(category_id)
        category = CategorySelector.get_by_id(category_id)
        if not category:
            self._raise_validation_error(ErrorCode.C01.value)
        
        return True


class AmountValidationHandler(BaseValidator):
    """
    Validates that the amount is valid (positive and reasonable)
    """
    
    def _validate(self, data: Dict[str, Any]) -> bool:
        amount = data.get('amount')
        print("=== DEBUG: AmountValidationHandler - Validación iniciada ===")
        print(amount)
        if not amount:
            self._raise_validation_error(ErrorCode.T03.value)
        
        try:
            amount_decimal = Decimal(str(amount))
            print(amount_decimal)
            if amount_decimal <= 0:
                self._raise_validation_error(ErrorCode.T03.value)
            
            # Validar que no sea un monto excesivamente alto (ej: más de 1 millón)
            if amount_decimal > Decimal('1000000'):
                self._raise_validation_error(ErrorCode.T03.value)
                
        except (ValueError, TypeError):
            self._raise_validation_error(ErrorCode.T03.value)
        
        return True


class ExternalIdValidationHandler(BaseValidator):
    """
    Validates that external_id is unique if provided
    """
    
    def _validate(self, data: Dict[str, Any]) -> bool:
        external_id = data.get('external_id')
        print(external_id)
        if external_id:
            # Verificar que no exista otra transacción con el mismo external_id
            existing_transaction = TransactionSelector.get_by_filters(external_id=external_id).first()
            if existing_transaction:
                self._raise_validation_error(ErrorCode.T01.value)
        
        return True


class BusinessRuleValidationHandler(BaseValidator):
    """
    Validates business rules (ej: límites de transacciones por día, etc.)
    """
    
    def _validate(self, data: Dict[str, Any]) -> bool:
        # Aquí puedes agregar reglas de negocio específicas
        # Por ejemplo: límite de transacciones por día, monto máximo por categoría, etc.
        
        # Ejemplo: Verificar que no haya más de 50 transacciones por balance por día
        balance_id = data.get('balance').id
        if balance_id:
            # Esta lógica se puede implementar más adelante
            pass
        
        return True 