import pytest
from app import create_app
from db import db

@pytest.fixture
def client():
    app = create_app()
    db.init_app(app)
    app.config["TESTING"] = True

    yield app.test_client()