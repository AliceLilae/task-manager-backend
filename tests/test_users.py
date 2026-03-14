from app.utils.security import verify_password
from app.models.user import User

def test_create_user(client, user_payload):

    response = client.post("/users", json=user_payload)

    assert response.status_code == 200

    data = response.json()

    assert data["email"] == user_payload["email"]
    assert data["name"] == user_payload["name"]
    

def test_password_is_hashed(client, user_payload, db):

    client.post("/users", json=user_payload)

    user = db.query(User).first()

    assert user.password_hash != user_payload["password_hash"]

    assert verify_password(
        user_payload["password_hash"],
        user.password_hash
    )
    
def test_create_user_duplicate_email(client, user_payload):

    client.post("/users", json=user_payload)

    response = client.post("/users", json=user_payload)

    assert response.status_code == 400
    assert response.json()["detail"] == "Email déjà utilisé"
    
def test_get_users(client, user):

    response = client.get("/users")

    assert response.status_code == 200

    data = response.json()

    assert len(data) == 1
    assert data[0]["email"] == user.email
    
def test_get_user_by_id(client, user):

    response = client.get(f"/users/{user.id}")

    assert response.status_code == 200

    data = response.json()

    assert data["id"] == user.id
    
def test_get_user_not_found(client):

    response = client.get("/users/999")

    assert response.status_code == 404
    
def test_delete_user(client, user):

    response = client.delete(f"/users/{user.id}")

    assert response.status_code == 200

    response = client.get("/users")

    data = response.json()

    assert data == []
    
def test_delete_user_already_deleted(client, user):

    client.delete(f"/users/{user.id}")

    response = client.delete(f"/users/{user.id}")

    assert response.status_code == 400