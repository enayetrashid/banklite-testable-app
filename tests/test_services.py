from app.repositories.storage import InMemoryStorage
from app.services.account_service import deposit_money


def test_deposit_money_updates_balance():
    storage = InMemoryStorage()

    new_balance, error_message = deposit_money(storage, "customer1", "50")

    assert error_message is None
    assert new_balance == 1050.0
