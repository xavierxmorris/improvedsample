"""
Integration tests for the BankAccount class with NotificationSystem.
Demonstrates testing interactions between components using mocks.
"""

import unittest
from unittest.mock import Mock
from bank_account import BankAccount


class TestBankAccountIntegration(unittest.TestCase):
    """Integration test cases for BankAccount with NotificationSystem."""

    def setUp(self) -> None:
        """Set up test fixtures with a mock notification system."""
        self.notification_system = Mock()

    # ===== Deposit Integration Tests =====

    def test_deposit_with_notification(self) -> None:
        """Test that a valid deposit triggers the notification system."""
        account = BankAccount(initial_balance=100, notification_system=self.notification_system)
        account.deposit(50)
        self.assertEqual(account.get_balance(), 150)
        self.notification_system.notify.assert_called_once_with("Deposited 50, new balance: 150")

    def test_deposit_negative_amount_no_notification(self) -> None:
        """Test that an invalid deposit does not trigger the notification system."""
        account = BankAccount(initial_balance=100, notification_system=self.notification_system)
        with self.assertRaises(ValueError):
            account.deposit(-50)
        self.notification_system.notify.assert_not_called()

    def test_deposit_zero_amount_no_notification(self) -> None:
        """Test that depositing zero does not trigger the notification system."""
        account = BankAccount(initial_balance=100, notification_system=self.notification_system)
        with self.assertRaises(ValueError):
            account.deposit(0)
        self.notification_system.notify.assert_not_called()

    def test_multiple_deposits_multiple_notifications(self) -> None:
        """Test that multiple deposits trigger multiple notifications."""
        account = BankAccount(initial_balance=0, notification_system=self.notification_system)
        account.deposit(100)
        account.deposit(50)
        self.assertEqual(self.notification_system.notify.call_count, 2)
        self.notification_system.notify.assert_any_call("Deposited 100, new balance: 100")
        self.notification_system.notify.assert_any_call("Deposited 50, new balance: 150")

    # ===== Withdrawal Integration Tests =====

    def test_withdraw_with_notification(self) -> None:
        """Test that a valid withdrawal triggers the notification system."""
        account = BankAccount(initial_balance=100, notification_system=self.notification_system)
        account.withdraw(30)
        self.assertEqual(account.get_balance(), 70)
        self.notification_system.notify.assert_called_once_with("Withdrew 30, new balance: 70")

    def test_withdraw_negative_amount_no_notification(self) -> None:
        """Test that an invalid withdrawal does not trigger the notification system."""
        account = BankAccount(initial_balance=100, notification_system=self.notification_system)
        with self.assertRaises(ValueError):
            account.withdraw(-30)
        self.notification_system.notify.assert_not_called()

    def test_withdraw_zero_amount_no_notification(self) -> None:
        """Test that withdrawing zero does not trigger the notification system."""
        account = BankAccount(initial_balance=100, notification_system=self.notification_system)
        with self.assertRaises(ValueError):
            account.withdraw(0)
        self.notification_system.notify.assert_not_called()

    def test_withdraw_exceeds_balance_no_notification(self) -> None:
        """Test that overdraft attempt does not trigger the notification system."""
        account = BankAccount(initial_balance=100, notification_system=self.notification_system)
        with self.assertRaises(ValueError):
            account.withdraw(200)
        self.notification_system.notify.assert_not_called()

    def test_withdraw_exact_balance_with_notification(self) -> None:
        """Test that withdrawing exact balance triggers notification correctly."""
        account = BankAccount(initial_balance=100, notification_system=self.notification_system)
        account.withdraw(100)
        self.assertEqual(account.get_balance(), 0)
        self.notification_system.notify.assert_called_once_with("Withdrew 100, new balance: 0")

    # ===== Mixed Operations Integration Tests =====

    def test_deposit_and_withdraw_sequence(self) -> None:
        """Test a sequence of deposits and withdrawals with notifications."""
        account = BankAccount(initial_balance=50, notification_system=self.notification_system)
        account.deposit(100)
        account.withdraw(30)
        account.deposit(20)
        
        self.assertEqual(account.get_balance(), 140)
        self.assertEqual(self.notification_system.notify.call_count, 3)

    # ===== No Notification System Tests =====

    def test_deposit_without_notification_system(self) -> None:
        """Test that deposits work without a notification system."""
        account = BankAccount(initial_balance=100)
        account.deposit(50)
        self.assertEqual(account.get_balance(), 150)

    def test_withdraw_without_notification_system(self) -> None:
        """Test that withdrawals work without a notification system."""
        account = BankAccount(initial_balance=100)
        account.withdraw(30)
        self.assertEqual(account.get_balance(), 70)


if __name__ == '__main__':
    unittest.main()
