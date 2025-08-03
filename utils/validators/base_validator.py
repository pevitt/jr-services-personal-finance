from abc import ABC, abstractmethod
from typing import Optional, Any
from utils.exceptions import FinanceAPIException


class BaseValidator(ABC):
    """
    Base validator class for Chain of Responsibility pattern
    """
    
    def __init__(self):
        self._next_validator: Optional['BaseValidator'] = None
    
    def set_next(self, validator: 'BaseValidator') -> 'BaseValidator':
        """
        Set the next validator in the chain
        """
        self._next_validator = validator
        return self  # ← Retornar self, no validator
    
    def validate(self, data: Any) -> bool:
        """
        Execute validation and pass to next validator if exists
        """
        try:
            if self._validate(data):
                if self._next_validator:
                    return self._next_validator.validate(data)
                return True
            return False
        except Exception as e:
            # Re-lanzar la excepción para que se propague
            raise e
    
    @abstractmethod
    def _validate(self, data: Any) -> bool:
        """
        Implement the actual validation logic
        Returns True if validation passes, False otherwise
        """
        pass
    
    def _raise_validation_error(self, error_code: dict):
        """
        Helper method to raise validation errors
        """
        raise FinanceAPIException(error_code) 