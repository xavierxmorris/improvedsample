# Bank Account Testing Sample

This sample demonstrates how to write unit and integration tests using GitHub Copilot. It showcases best practices for:

- **Unit Testing**: Testing individual methods in isolation
- **Integration Testing**: Testing interactions between components using mocks
- **Edge Case Coverage**: Handling boundary conditions and invalid inputs
- **Exception Testing**: Verifying proper error handling

## Files

| File | Description |
|------|-------------|
| `bank_account.py` | The BankAccount class with deposit, withdraw, and notification features |
| `test_bank_account.py` | Unit tests covering all BankAccount functionality |
| `test_bank_account_integration.py` | Integration tests using mocks for NotificationSystem |

## Running the Tests

### Run Unit Tests

```bash
cd samples/bank_account
python -m unittest test_bank_account.py -v
```

### Run Integration Tests

```bash
cd samples/bank_account
python -m unittest test_bank_account_integration.py -v
```

### Run All Tests

```bash
cd samples/bank_account
python -m unittest discover -v
```

## Test Coverage

### Unit Tests (`test_bank_account.py`)

- Initial balance (default and custom)
- Valid deposits and withdrawals
- Multiple transactions
- Invalid amounts (negative, zero)
- Overdraft attempts
- Exception messages validation

### Integration Tests (`test_bank_account_integration.py`)

- NotificationSystem called on successful deposits
- NotificationSystem called on successful withdrawals
- NotificationSystem NOT called on failed transactions
- Multiple notifications for multiple transactions
- Behavior without NotificationSystem (graceful handling)

## Using Copilot to Generate Tests

### Example Prompts

**For Unit Tests:**
> "Develop a comprehensive suite of unit tests for the BankAccount class in Python. Write multiple test methods that cover a wide range of scenarios, including edge cases, exception handling, and data validation."

**For Integration Tests:**
> "Write integration tests for the deposit function in the BankAccount class. Use mocks to simulate the NotificationSystem and verify that it is called correctly after a deposit."

**For Improving Coverage:**
> "What additional tests should be included to ensure full coverage for the integration between the BankAccount class and the NotificationSystem?"

## Key Testing Patterns Demonstrated

### 1. Setup and Teardown
```python
def setUp(self):
    self.account = BankAccount()
```

### 2. Exception Testing
```python
def test_deposit_negative_amount_raises_error(self):
    with self.assertRaises(ValueError) as context:
        self.account.deposit(-100)
    self.assertEqual(str(context.exception), "Deposit amount must be positive.")
```

### 3. Mock Verification
```python
def test_deposit_with_notification(self):
    account = BankAccount(initial_balance=100, notification_system=self.notification_system)
    account.deposit(50)
    self.notification_system.notify.assert_called_once_with("Deposited 50, new balance: 150")
```

### 4. Negative Mock Verification
```python
def test_deposit_negative_amount_no_notification(self):
    with self.assertRaises(ValueError):
        account.deposit(-50)
    self.notification_system.notify.assert_not_called()
```
