from app import create_app



def test_login_api_returns_success_for_valid_user():
    app = create_app()
    client = app.test_client()

    response = client.post(
        "/api/login",
        json={"username": "customer1", "password": "Pass123!"},
    )

    data = response.get_json()

    assert response.status_code == 200
    assert data["success"] is True
    assert data["account_id"] == "A1001"



def test_balance_api_returns_current_balance():
    app = create_app()
    client = app.test_client()

    response = client.get("/api/accounts/A1001/balance")
    data = response.get_json()

    assert response.status_code == 200
    assert data["balance"] == 1000.0



def test_deposit_api_updates_balance():
    app = create_app()
    client = app.test_client()

    response = client.post(
        "/api/accounts/A1001/deposit",
        json={"amount": "50"},
    )
    data = response.get_json()

    assert response.status_code == 200
    assert data["new_balance"] == 1050.0
