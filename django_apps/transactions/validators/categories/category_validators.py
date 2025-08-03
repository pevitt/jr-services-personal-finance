from typing import Any, Dict
from django_apps.transactions.selectors import CategorySelector
from utils.validators.base_validator import BaseValidator
from utils.exceptions import ErrorCode


class CategoryNameValidationHandler(BaseValidator):
    """
    Validates that category name is not empty and has valid format
    """
    
    def _validate(self, data: Dict[str, Any]) -> bool:
        name = data.get('name')
        if not name or not name.strip():
            self._raise_validation_error(ErrorCode.C00.value)
        
        # Validar longitud mínima y máxima
        if len(name.strip()) < 2:
            self._raise_validation_error(ErrorCode.C00.value)
        
        if len(name.strip()) > 100:
            self._raise_validation_error(ErrorCode.C00.value)
        
        return True


class CategoryTypeValidationHandler(BaseValidator):
    """
    Validates that category type is valid
    """
    
    def _validate(self, data: Dict[str, Any]) -> bool:
        category_type = data.get('type')
        valid_types = ['income', 'expenses']
        
        if not category_type or category_type not in valid_types:
            self._raise_validation_error(ErrorCode.C00.value)
        
        return True


class CategoryUniquenessValidationHandler(BaseValidator):
    """
    Validates that category name and type combination is unique
    """
    
    def _validate(self, data: Dict[str, Any]) -> bool:
        name = data.get('name')
        category_type = data.get('type')
        
        if name and category_type:
            existing_category = CategorySelector.get_by_filters(
                name=name.strip(), 
                type=category_type
            ).first()
            
            if existing_category:
                self._raise_validation_error(ErrorCode.C04.value)
        
        return True


class CategoryExistenceValidationHandler(BaseValidator):
    """
    Validates that category exists when updating/deleting
    """
    
    def _validate(self, data: Dict[str, Any]) -> bool:
        category_id = data.get('category_id')
        if not category_id:
            self._raise_validation_error(ErrorCode.C03.value)
        
        category = CategorySelector.get_by_id(category_id)
        if not category:
            self._raise_validation_error(ErrorCode.C03.value)
        
        return True 