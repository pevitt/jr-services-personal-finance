# utils/selectors/base_selector.py
from abc import ABC, abstractmethod
from typing import Any, List, Optional
from django.db import models

class BaseSelector(ABC):
    """
    Clase base para todos los selectors.
    Define métodos comunes para consultas y CRUD básico.
    """
    
    model = None  # Debe ser definido en las clases hijas
    
    @classmethod
    def create(cls, **kwargs) -> models.Model:
        """Crear un nuevo registro"""
        if not cls.model:
            raise NotImplementedError("Model must be defined in subclass")
        return cls.model.objects.create(**kwargs)
    
    @classmethod
    def update(cls, instance: models.Model, **kwargs) -> models.Model:
        """Actualizar un registro existente"""
        for key, value in kwargs.items():
            setattr(instance, key, value)
        instance.save()
        return instance
    
    @classmethod
    def delete(cls, instance: models.Model) -> bool:
        """Eliminar un registro"""
        instance.delete()
        return True
    
    @classmethod
    def get_by_id(cls, id: Any) -> Optional[models.Model]:
        """Obtener por ID"""
        if not cls.model:
            raise NotImplementedError("Model must be defined in subclass")
        return cls.model.objects.filter(id=id).first()
    
    @classmethod
    def get_all(cls) -> List[models.Model]:
        """Obtener todos los registros"""
        if not cls.model:
            raise NotImplementedError("Model must be defined in subclass")
        return cls.model.objects.all()
    
    @classmethod
    def filter(cls, **filters) -> List[models.Model]:
        """Filtrar registros por cualquier campo"""
        if not cls.model:
            raise NotImplementedError("Model must be defined in subclass")
        return cls.model.objects.filter(**filters)
    
    @classmethod
    def get_or_create(cls, defaults=None, **kwargs) -> tuple[models.Model, bool]:
        """Obtener o crear si no existe"""
        if not cls.model:
            raise NotImplementedError("Model must be defined in subclass")
        return cls.model.objects.get_or_create(defaults=defaults, **kwargs)
    
    @classmethod
    def bulk_create(cls, objects: List[models.Model]) -> List[models.Model]:
        """Crear múltiples registros"""
        if not cls.model:
            raise NotImplementedError("Model must be defined in subclass")
        return cls.model.objects.bulk_create(objects)
    
    @classmethod
    def count(cls, **filters) -> int:
        """Contar registros que cumplan los filtros"""
        if not cls.model:
            raise NotImplementedError("Model must be defined in subclass")
        return cls.model.objects.filter(**filters).count()
    
    @classmethod
    def exists(cls, **filters) -> bool:
        """Verificar si existe algún registro con los filtros"""
        if not cls.model:
            raise NotImplementedError("Model must be defined in subclass")
        return cls.model.objects.filter(**filters).exists()