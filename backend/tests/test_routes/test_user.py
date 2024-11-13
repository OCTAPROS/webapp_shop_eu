def test_create_user(client):
    data = {
        "email": "test@example.com",
        "password": "secretpassword123"
    }
    response = client.post("/users/", json=data)

    assert response.status_code == 201
    assert response.json()["email"] == data["email"]