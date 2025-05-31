import pytest
import requests

pytestmark = pytest.mark.api
EXPECTED_CATEGORIES = [
    {"id": 1, "name": "Starter"},
    {"id": 2, "name": "Main"},
    {"id": 3, "name": "Dessert"},
    {"id": 4, "name": "Beverage"}
]

def test_public_api_get_recipe():
    url = "https://localhost:7175/api/Recipes/getrecipe/1"
    response = requests.get(url, verify=False)

    assert response.status_code == 200
    data = response.json()
    assert data["id"] == 1
    assert data["name"] == "Breadless Philly Cheese Steak"


def test_public_api_get_all_categories():
    url = "https://localhost:7175/api/getallcategories"
    response = requests.get(url, verify=False)

    assert response.status_code == 200
    data = response.json()
    shortened_response = data[:4]

    assert shortened_response == EXPECTED_CATEGORIES, f"Difference in expected response: {shortened_response}"
    assert data[3]['name'] == "Beverage", f"Expected 'Beverage' but got '{data[3]['name']}' instead."


