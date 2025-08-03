from typing import Dict, Any
from utils.validators.base_validator import BaseValidator
from django_apps.transactions.validators.transactions.transaction_validators import (
    BalanceValidationHandler,
    CategoryValidationHandler,
    AmountValidationHandler,
    ExternalIdValidationHandler,
    BusinessRuleValidationHandler
)


class TransactionValidationChain:
    """
    Chain of Responsibility for transaction validation
    """
    
    def __init__(self):
        # Crear la cadena de validadores
        self.balance_validator = BalanceValidationHandler()
        self.category_validator = CategoryValidationHandler()
        self.amount_validator = AmountValidationHandler()
        self.external_id_validator = ExternalIdValidationHandler()
        self.business_rule_validator = BusinessRuleValidationHandler()
        
        # Configurar la cadena
        self.balance_validator.set_next(
            self.category_validator.set_next(
                self.amount_validator.set_next(
                    self.external_id_validator.set_next(
                        self.business_rule_validator
                    )
                )
            )
        )
        
    
    def validate(self, data: Dict[str, Any]) -> bool:
        """
        Execute the entire validation chain
        """
        return self.balance_validator.validate(data)
    
    def get_validator_chain(self) -> BaseValidator:
        """
        Get the first validator in the chain
        """
        return self.balance_validator


# Factory method para crear la cadena de validación
def create_transaction_validation_chain() -> TransactionValidationChain:
    """
    Factory method to create a transaction validation chain
    """
    return TransactionValidationChain() 