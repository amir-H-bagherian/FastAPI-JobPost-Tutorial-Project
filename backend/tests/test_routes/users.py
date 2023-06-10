from fastapi import status


def test_create_user(client):
    data = {"username": "amir", "password": "1234", "email": "amir@gmail.com"}
    response = client.post('/users/', json=data)
    assert response.status_code == status.HTTP_200_OK
    assert response.json()['is_active'] == True
    assert response.json()['email'] == "amir@gmail.com"