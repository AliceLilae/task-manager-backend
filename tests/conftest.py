from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from fastapi.testclient import TestClient

from app.database import Base, get_db
from app.models import user, task
from app.main import app

import pytest
import os

TEST_DATABASE_URL = os.getenv("TEST_DATABASE_URL")

engine = create_engine(TEST_DATABASE_URL)

TestingSessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
)

@pytest.fixture(scope="function")
def db():

    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)

    connection = engine.connect()
    transaction = connection.begin()

    session = TestingSessionLocal(bind=connection)

    yield session

    session.close()

    if transaction.is_active:
        transaction.rollback()

    connection.close()

@pytest.fixture(scope="function")
def client(db):

    def override_get_db():
        yield db

    app.dependency_overrides[get_db] = override_get_db

    yield TestClient(app)

    app.dependency_overrides.clear()
    
from tests.fixtures.users import *
from tests.fixtures.tasks import *
from tests.fixtures.payloads import *