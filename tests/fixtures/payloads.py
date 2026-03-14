import pytest


@pytest.fixture
def user_payload():
    return {
        "name": "Test User",
        "username": "testuser",
        "email": "test@test.com",
        "password_hash": "password123"
    }


@pytest.fixture
def task_payload(user):
    return {
        "title": "Test task",
        "description": "testing api",
        "status": "pending",
        "user_id": user.id
    }