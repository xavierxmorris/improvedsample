"""
Unit tests for the BankAccount class.
Demonstrates comprehensive test coverage including edge cases, exception handling, and data validation.
"""

import unittest
from bank_account import BankAccount


class TestBankAccount(unittest.TestCase):
    """Test cases for the BankAccount class."""

    def setUp(self) -> None:
        """Set up test fixtures before each test method."""
        self.account = BankAccount()

    def test_initial_balance_default(self) -> None:
        """Test that the default initial balance is zero."""
        self.assertEqual(self.account.get_balance(), 0)

    def test_initial_balance_with_value(self) -> None:
        """Test creating an account with a specific initial balance."""
        account = BankAccount(initial_balance=100)
        self.assertEqual(account.get_balance(), 100)

    def test_deposit_positive_amount(self) -> None:
        """Test depositing a positive amount increases the balance."""
        self.account.deposit(100)
        self.assertEqual(self.account.get_balance(), 100)

    def test_deposit_multiple_times(self) -> None:
        """Test multiple deposits accumulate correctly."""
        self.account.deposit(100)
        self.account.deposit(50)
        self.assertEqual(self.account.get_balance(), 150)

    def test_withdraw_within_balance(self) -> None:
        """Test withdrawing an amount within the available balance."""
        self.account.deposit(100)
        self.account.withdraw(50)
        self.assertEqual(self.account.get_balance(), 50)

    def test_withdraw_exact_balance(self) -> None:
        """Test withdrawing the exact balance leaves zero."""
        self.account.deposit(100)
        self.account.withdraw(100)
        self.assertEqual(self.account.get_balance(), 0)

    def test_deposit_negative_amount_raises_error(self) -> None:
        """Test that depositing a negative amount raises ValueError."""
        with self.assertRaises(ValueError) as context:
            self.account.deposit(-100)
        self.assertEqual(str(context.exception), "Deposit amount must be positive.")

    def test_deposit_zero_amount_raises_error(self) -> None:
        """Test that depositing zero raises ValueError."""
        with self.assertRaises(ValueError) as context:
            self.account.deposit(0)
        self.assertEqual(str(context.exception), "Deposit amount must be positive.")

    def test_withdraw_negative_amount_raises_error(self) -> None:
        """Test that withdrawing a negative amount raises ValueError."""
        with self.assertRaises(ValueError) as context:
            self.account.withdraw(-50)
        self.assertEqual(str(context.exception), "Withdrawal amount must be positive.")

    def test_withdraw_zero_amount_raises_error(self) -> None:
        """Test that withdrawing zero raises ValueError."""
        with self.assertRaises(ValueError) as context:
            self.account.withdraw(0)
        self.assertEqual(str(context.exception), "Withdrawal amount must be positive.")

    def test_withdraw_more_than_balance_raises_error(self) -> None:
        """Test that withdrawing more than balance raises ValueError."""
        self.account.deposit(100)
        with self.assertRaises(ValueError) as context:
            self.account.withdraw(200)
        self.assertEqual(str(context.exception), "Cannot withdraw more than the current balance.")

    def test_initial_balance_negative_raises_error(self) -> None:
        """Test that creating an account with negative balance raises ValueError."""
        with self.assertRaises(ValueError) as context:
            BankAccount(-100)
        self.assertEqual(str(context.exception), "Initial balance cannot be negative.")

    def test_withdraw_from_empty_account_raises_error(self) -> None:
        """Test that withdrawing from an empty account raises ValueError."""
        with self.assertRaises(ValueError) as context:
            self.account.withdraw(1)
        self.assertEqual(str(context.exception), "Cannot withdraw more than the current balance.")


if __name__ == '__main__':
    unittest.main()
