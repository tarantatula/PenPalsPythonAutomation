import pytest

pytestmark = pytest.mark.api
import requests


def test_public_api_get_post():
    url = "https://localhost:7175/api/Recipes/getrecipe/1"
    response = requests.get(url, verify=False)

    assert response.status_code == 200
    data = response.json()
    assert data["id"] == 1
    assert data["name"] == "Breadless Philly Cheese Steak"
