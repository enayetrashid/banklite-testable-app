from app.repositories.storage import InMemoryStorage
from app.services.account_service import deposit_money
from app.services.account_service import withdraw_money


def test_deposit_money_updates_balance():
    storage = InMemoryStorage()

    new_balance, error_message = deposit_money(storage, "customer1", "50")

    assert error_message is None
    assert new_balance == 1050.0


def test_withdraw_money_blocks_insufficient_funds():
    storage = InMemoryStorage()

    new_balance, error_message = withdraw_money(storage, "customer2", "1000")

    assert new_balance is None
    assert error_message == "Insufficient funds."
