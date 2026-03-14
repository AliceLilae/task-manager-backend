import pytest
from datetime import datetime, UTC

from app.models.task import Task, Status


@pytest.fixture
def task(db, user):
    task = Task(
        title="Test Task",
        description="Testing",
        status=Status.PENDING,
        user_id=user.id,
        created_at=datetime.now(UTC),
        updated_at=datetime.now(UTC),
    )

    db.add(task)
    db.commit()
    db.refresh(task)

    return task