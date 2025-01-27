from beerlog.api import api
from fastapi.testclient import TestClient

client = TestClient(api)


def test_create_beer():
    response = client.post(
        "/beers",
        json={
            "name": "Skol",
            "style": "KornPA",
            "flavor": 1,
            "image": 1,
            "cost": 2,
        },
    )
    assert response.status_code == 201
    result = response.json()
    assert result["name"] == "Skol"
    assert result["id"] == 1


def test_list_beers():
    response = client.get("/beers")
    assert response.status_code == 200
    result = response.json()
    assert len(result) == 0
