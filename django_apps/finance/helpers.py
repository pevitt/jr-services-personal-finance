from django_apps.finance.selectors import BudgetSelector


def update_budget_actual_savings(user, new_balance_amount):
    """
    Helper function to update budget's actual_savings when balance changes
    
    Args:
        user: User instance or user ID
        new_balance_amount: New available balance amount
    """
    try:
        budget = BudgetSelector.get_by_filters(user=user).first()
        if budget:
            budget.actual_savings = new_balance_amount
            budget.save()
            print(f"=== DEBUG: Budget actual_savings updated to {new_balance_amount} for user {user} ===")
        else:
            print(f"=== DEBUG: No budget found for user {user} ===")
    except Exception as e:
        print(f"=== DEBUG: Error updating budget: {e} ===") 