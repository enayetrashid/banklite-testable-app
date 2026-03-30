from copy import deepcopy


class InMemoryStorage:
    def __init__(self):
        self.users = {
            "customer1": {
                "password": "Pass123!",
                "full_name": "Customer One",
                "account_id": "A1001",
                "balance": 1000.0,
                "transactions": [],
            },
            "customer2": {
                "password": "Pass123!",
                "full_name": "Customer Two",
                "account_id": "A1002",
                "balance": 500.0,
                "transactions": [],
            },
        }

    def get_user(self, username):
        return self.users.get(username)

    def get_user_by_account_id(self, account_id):
        for username, user in self.users.items():
            if user["account_id"] == account_id:
                return username, user
        return None, None

    def update_balance(self, username, new_balance):
        user = self.get_user(username)
        if user is None:
            return
        user["balance"] = new_balance

    def add_transaction(self, username, transaction):
        user = self.get_user(username)
        if user is None:
            return
        user["transactions"].append(transaction)

    def list_transactions(self, username):
        user = self.get_user(username)
        if user is None:
            return []
        return deepcopy(user["transactions"])
