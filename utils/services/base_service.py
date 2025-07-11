# utils/services/base_service.py
from abc import ABC, abstractmethod
from typing import Any, Dict, List, Optional
from django.db import models

class BaseService(ABC):
    """
    Clase base para todos los servicios.
    Define métodos comunes que deben implementar los servicios específicos.
    """
    
    @classmethod
    @abstractmethod
    def create(cls, **kwargs) -> models.Model:
        """Crear un nuevo registro"""
        pass
    
    @classmethod
    @abstractmethod
    def update(cls, instance: models.Model, **kwargs) -> models.Model:
        """Actualizar un registro existente"""
        pass
    
    @classmethod
    @abstractmethod
    def delete(cls, instance: models.Model) -> bool:
        """Eliminar un registro"""
        pass
    
    @classmethod
    @abstractmethod
    def get_by_id(cls, id: Any) -> Optional[models.Model]:
        """Obtener por ID"""
        pass
    
    @classmethod
    @abstractmethod
    def get_all(cls) -> List[models.Model]:
        """Obtener todos los registros"""
        pass
    
    @classmethod
    def validate_data(cls, data: Dict) -> bool:
        """Validación común de datos"""
        return True
    
    @classmethod
    def process_before_save(cls, data: Dict) -> Dict:
        """Procesar datos antes de guardar"""
        return data
    
    @classmethod
    def process_after_save(cls, instance: models.Model) -> models.Model:
        """Procesar después de guardar"""
        return instance