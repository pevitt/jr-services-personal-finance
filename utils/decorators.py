from functools import wraps
import uuid
from utils.exceptions import FinanceAPIException, ErrorCode

def validate_uuid_param(param_name):
    """
    Decorador para validar que un parámetro de la URL sea un UUID válido.
    
    Uso:
    @validate_uuid_param('balance_id')
    def get(self, request, balance_id):
        # balance_id ya está validado como UUID
        pass
    """
    def decorator(func):
        @wraps(func)
        def wrapper(self, request, *args, **kwargs):
            # Obtener el valor del parámetro
            param_value = str(kwargs.get(param_name))
            
            if param_value:
                try:
                    # Validar que sea un UUID válido
                    uuid.UUID(param_value)
                except ValueError:
                    raise FinanceAPIException(
                        error_code=ErrorCode.B04.value,
                        message=f"Invalid UUID format for {param_name}"
                    )
            
            # Si es válido, continuar con la función original
            return func(self, request, *args, **kwargs)
        return wrapper
    return decorator