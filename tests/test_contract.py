import requests
import pytest

class CategoriesApi:
    def __init__(self, base_url):
        self.base_url = base_url

    def get_categories(self):
        response = requests.get(f"{self.base_url}/products/categories")
        response.raise_for_status()
        return response.json()


@pytest.fixture
def categories_api():
    return CategoriesApi("https://dummyjson.com")


def test_contract_categories_endpoint(categories_api):
    expected_categories = [
        "smartphones",
        "laptops",
        "fragrances",
        "skincare",
        "groceries",
        "home-decoration",
        "furniture",
        "tops",
        "womens-dresses",
        "womens-shoes",
        "mens-shirts",
        "mens-shoes",
        "mens-watches",
        "womens-watches",
        "womens-bags",
        "womens-jewellery",
        "sunglasses",
        "automotive",
        "motorcycle",
        "lighting",
    ]
    assert categories_api.get_categories() == expected_categories
