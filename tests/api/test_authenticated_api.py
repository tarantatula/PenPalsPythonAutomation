import pytest
import requests

pytestmark = pytest.mark.api
NEW_RECIPE = [
    {
        "name": "Cup of Milk",
        "description": "A good old cup of milk",
        "categoryId": 0,
        "instructions": "Pour the milk into a cup and enjoy",
        "ingredients": [
            {
                "name": "Milk",
                "quantity": 1,
                "uom": "c"
            }
        ]
    }
]


@pytest.fixture
def auth_token():
    """Fixture to fetch and return the token once."""
    url = "https://localhost:7175/api/Users/getAccessToken"
    credentials = {"username": "tarantula2", "password": "12345"}
    response = requests.post(url, json=credentials, verify=False)
    assert response.status_code == 200
    return response.json()["token"]


def test_1_get_recipes_for_current_user(auth_token):
    url = "https://localhost:7175/api/Recipes/getrecipesforcurrentuser"
    headers = {"Authorization": f"Bearer {auth_token}"}
    response = requests.get(url, headers=headers, verify=False)
    assert response.status_code == 200, response.status_code
    assert len(response.json()) > 1, response.json()


def test_2_add_recipes(auth_token):
    global NEW_RECIPE
    url = "https://localhost:7175/api/Recipes/addrecipes"
    headers = {
        "Authorization": f"Bearer {auth_token}",
        "Content-Type": "application/json"
    }
    response = requests.put(url, json=NEW_RECIPE, headers=headers, verify=False)
    assert response.status_code == 201, f"Bad response: {response.status_code}"
    recipe_ids = response.json()["recipeIds"]
    assert len(recipe_ids) == 1, f"number of IDs is not equal{recipe_ids}"
    NEW_RECIPE[0]["id"] = recipe_ids[0]


def test_3_delete_recipe(auth_token):
    delete_recipe_id = NEW_RECIPE[0]["id"]
    url = "https://localhost:7175/api/Recipes/deleteRecipe/"+str(delete_recipe_id)
    headers = {
        "Authorization": f"Bearer {auth_token}"
    }
    response = requests.delete(url, headers=headers, verify=False)
    assert response.status_code == 204, response.status_code

