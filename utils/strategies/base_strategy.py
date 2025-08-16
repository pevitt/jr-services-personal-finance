from abc import ABC, abstractmethod
from decimal import Decimal
from typing import Dict, Any


class BaseSavingsStrategy(ABC):
    """
    Base strategy class for savings calculation
    """
    
    @abstractmethod
    def calculate_suggested_savings(self, monthly_income: Decimal) -> Decimal:
        """
        Calculate suggested savings based on monthly income
        
        Args:
            monthly_income: Monthly income amount
            
        Returns:
            Suggested savings amount
        """
        pass
    
    def get_strategy_name(self) -> str:
        """
        Get the name of the strategy
        
        Returns:
            Strategy name
        """
        return self.__class__.__name__
    
    def get_strategy_description(self) -> str:
        """
        Get description of the strategy
        
        Returns:
            Strategy description
        """
        return "Base savings strategy" 