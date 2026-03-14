import pytest
from datetime import datetime, UTC

from app.models.user import User


@pytest.fixture
def user(db):
    user = User(
        name="Test User",
        username="testuser",
        email="test@test.com",
        password_hash="hash",
        created_at=datetime.now(UTC),
        updated_at=datetime.now(UTC),
    )

    db.add(user)
    db.commit()
    db.refresh(user)

    return user