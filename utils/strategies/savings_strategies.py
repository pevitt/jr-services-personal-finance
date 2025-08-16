from decimal import Decimal
from utils.strategies.base_strategy import BaseSavingsStrategy


class ConservativeStrategy(BaseSavingsStrategy):
    """
    Conservative savings strategy: 30% of monthly income
    """
    
    def calculate_suggested_savings(self, monthly_income: Decimal) -> Decimal:
        """
        Calculate 30% of monthly income as suggested savings
        """
        return monthly_income * Decimal("0.30")
    
    def get_strategy_description(self) -> str:
        return "Conservative approach: Save 30% of monthly income"


class BalancedStrategy(BaseSavingsStrategy):
    """
    Balanced savings strategy: 40% of monthly income
    """
    
    def calculate_suggested_savings(self, monthly_income: Decimal) -> Decimal:
        """
        Calculate 40% of monthly income as suggested savings
        """
        return monthly_income * Decimal("0.40")
    
    def get_strategy_description(self) -> str:
        return "Balanced approach: Save 40% of monthly income"


class AggressiveStrategy(BaseSavingsStrategy):
    """
    Aggressive savings strategy: 50% of monthly income
    """
    
    def calculate_suggested_savings(self, monthly_income: Decimal) -> Decimal:
        """
        Calculate 50% of monthly income as suggested savings
        """
        return monthly_income * Decimal("0.50")
    
    def get_strategy_description(self) -> str:
        return "Aggressive approach: Save 50% of monthly income"



class SavingsStrategyFactory:
    """
    Factory class to create savings strategies
    """
    
    @staticmethod
    def create_strategy(strategy_name: str, **kwargs) -> BaseSavingsStrategy:
        """
        Create a savings strategy based on strategy name
        
        Args:
            strategy_name: Name of the strategy
            **kwargs: Additional parameters for custom strategy
            
        Returns:
            Strategy instance
        """
        strategy_map = {
            'conservative': ConservativeStrategy,
            'balanced': BalancedStrategy,
            'aggressive': AggressiveStrategy
        }
        
        if strategy_name not in strategy_map:
            raise ValueError(f"Unknown strategy: {strategy_name}")
        
        strategy_class = strategy_map[strategy_name]
        
        if strategy_name == 'custom':
            percentage = kwargs.get('percentage')
            if not percentage:
                raise ValueError("Custom strategy requires 'percentage' parameter")
            return strategy_class(Decimal(str(percentage)))
        
        return strategy_class() 