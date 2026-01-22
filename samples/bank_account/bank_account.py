"""
Bank Account module demonstrating a simple banking class.
This module is used as an example for writing unit and integration tests with GitHub Copilot.
"""


class BankAccount:
    """
    A simple bank account class that supports deposits, withdrawals, and balance inquiries.
    Optionally integrates with a notification system for transaction alerts.
    
    Attributes:
        balance (float): The current account balance.
        notification_system: Optional notification service for sending transaction alerts.
    """

    def __init__(self, initial_balance: float = 0, notification_system=None) -> None:
        """
        Initialize a new BankAccount instance.
        
        Args:
            initial_balance: The starting balance for the account. Defaults to 0.
            notification_system: Optional notification service for transaction alerts.
        
        Raises:
            ValueError: If initial_balance is negative.
        """
        if initial_balance < 0:
            raise ValueError("Initial balance cannot be negative.")
        self.balance = initial_balance
        self.notification_system = notification_system

    def deposit(self, amount: float) -> None:
        """
        Deposit funds into the account.
        
        Args:
            amount: The amount to deposit. Must be positive.
        
        Raises:
            ValueError: If amount is zero or negative.
        """
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self.balance += amount
        if self.notification_system:
            self.notification_system.notify(f"Deposited {amount}, new balance: {self.balance}")

    def withdraw(self, amount: float) -> None:
        """
        Withdraw funds from the account.
        
        Args:
            amount: The amount to withdraw. Must be positive and not exceed balance.
        
        Raises:
            ValueError: If amount is zero or negative.
            ValueError: If amount exceeds the current balance.
        """
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if amount > self.balance:
            raise ValueError("Cannot withdraw more than the current balance.")
        self.balance -= amount
        if self.notification_system:
            self.notification_system.notify(f"Withdrew {amount}, new balance: {self.balance}")

    def get_balance(self) -> float:
        """
        Get the current account balance.
        
        Returns:
            float: The current balance.
        """
        return self.balance
