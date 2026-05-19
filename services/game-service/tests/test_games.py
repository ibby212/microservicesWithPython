import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

from app.main import app
from app.database import Base, get_db

engine = create_engine(
    "sqlite:///:memory:",
    connect_args={"check_same_thread": False},
    poolclass=StaticPool,
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


@pytest.fixture
def client():
    Base.metadata.create_all(bind=engine)

    def override_get_db():
        db = TestingSessionLocal()
        try:
            yield db
        finally:
            db.close()

    app.dependency_overrides[get_db] = override_get_db
    with TestClient(app) as c:
        yield c

    app.dependency_overrides.clear()
    Base.metadata.drop_all(bind=engine)


GAME_PAYLOAD = {
    "title": "Hollow Knight",
    "genre": "Metroidvania",
    "platform": "PC",
    "release_year": 2017,
}


def test_create_game_returns_201(client):
    response = client.post("/v1/games/", json=GAME_PAYLOAD)
    assert response.status_code == 201
    assert response.json()["title"] == "Hollow Knight"


def test_get_unknown_game_returns_404(client):
    response = client.get("/v1/games/nonexistent-id")
    assert response.status_code == 404


def test_search_games(client):
    client.post("/v1/games/", json=GAME_PAYLOAD)
    client.post("/v1/games/", json={**GAME_PAYLOAD, "title": "Celeste", "genre": "Platformer"})

    response = client.get("/v1/games/search?q=hollow")
    assert response.status_code == 200
    assert response.json()["total"] == 1
