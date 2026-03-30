from app import create_app


def test_login_api_returns_success_for_valid_user():
    app = create_app()
    client = app.test_client()

    response = client.post(
        "/api/login",
        json={"username": "customer1", "password": "Pass123!"},
    )

    assert response.status_code == 200
