import requests
import configparser
import pytest
import allure
import jsonschema
import os
from dotenv import load_dotenv

load_dotenv()

config = configparser.ConfigParser()
config.read("config.ini")
os.environ["REQUESTS_CA_BUNDLE"] = ""

api_key = os.getenv("TOKEN") or config.get("API", "TOKEN")
base_url = os.getenv("BASE_URL") or config.get("API", "BASE_URL")
email = os.getenv("EMAIL") or config.get("API", "EMAIL")
password = os.getenv("PASSWORD") or config.get("API", "PASSWORD")
headers = {"Authorization": f"Bearer token={api_key}"}


@allure.feature("Test Dummy JSON API")
class TestClass:
    @allure.story("Test GET all products")
    @allure.title("Verify the GET products")
    @allure.description("verify the GET API response status code and data")
    @allure.severity("blocker")
    def test_get_products(self):
        # Act
        response_raw = requests.get(f"{base_url}/products")
        assert (
            response_raw.status_code == 200
        ), f"Expected status code 200, but got {response_raw.status_code}"

        # Assert
        response = response_raw.json()

        schema = {
            "type": "object",
            "properties": {
                "products": {
                    "type": "array",
                    "items": {
                        "type": "object",
                        "properties": {
                            "id": {"type": "integer"},
                            "title": {"type": "string"},
                            "description": {"type": "string"},
                            "price": {"type": "integer"},
                            "discountPercentage": {"type": "number"},
                            "rating": {"type": "number"},
                            "stock": {"type": "integer"},
                            "brand": {"type": "string"},
                            "category": {"type": "string"},
                            "thumbnail": {"type": "string"},
                            "images": {"type": "array", "items": {"type": "string"}},
                        },
                        "required": [
                            "id",
                            "title",
                            "description",
                            "price",
                            "discountPercentage",
                            "rating",
                            "stock",
                            "brand",
                            "category",
                            "thumbnail",
                            "images",
                        ],
                    },
                },
                "total": {"type": "integer"},
                "skip": {"type": "integer"},
                "limit": {"type": "integer"},
            },
            "required": ["products", "total", "skip", "limit"],
        }
        try:
            jsonschema.validate(instance=response, schema=schema)
        except jsonschema.exceptions.ValidationError as e:
            assert False, f"Schema validation failed: {e}"
        assert True
        keys_to_assert = ["products", "total", "skip", "limit"]
        for key in keys_to_assert:
            assert (
                key in response
            ), f"Expected {key} to be in the dictionary, but it's not."
        assert isinstance(
            response["products"], list
        ), "Expected the object tobe a list, but it's not"
        assert (
            len(response["products"]) == 30
        ), "Expected the list to have length 30, but it's not"
        keys_to_assert = [
            "id",
            "title",
            "description",
            "price",
            "discountPercentage",
            "rating",
            "stock",
            "brand",
            "category",
            "thumbnail",
            "images",
        ]
        for key in keys_to_assert:
            assert (
                key in response["products"][0]
            ), f"Expected {key} to be in the dictionary, but it's not."
        assert (
            response["products"][0]["id"] == 1
        ), f'Expected {response["products"][0]["id"]} to be number 1, but it is not.'
        assert (
            response["products"][0]["title"] == "iPhone 9"
        ), f'Expected {response["products"][0]["title"]} to be string "iPhone 9", but it is not.'
        assert (
            response["products"][0]["description"]
            == "An apple mobile which is nothing like apple"
        ), f'Expected {response["products"][0]["description"]} to be string "An apple mobile which is nothing like apple", but it is not.'
        assert (
            response["products"][0]["price"] == 549
        ), f'Expected {response["products"][0]["price"]} to be number 549, but it is not.'
        assert (
            response["products"][0]["discountPercentage"] == 12.96
        ), f'Expected {response["products"][0]["discountPercentage"]} to be number 12.96, but it is not.'
        assert (
            response["products"][0]["rating"] == 4.69
        ), f'Expected {response["products"][0]["rating"]} to be number 4.69, but it is not.'
        assert (
            response["products"][0]["stock"] == 94
        ), f'Expected {response["products"][0]["stock"]} to be number 94, but it is not.'
        assert (
            response["products"][0]["brand"] == "Apple"
        ), f'Expected {response["products"][0]["brand"]} to be string "Apple", but it is not.'
        assert (
            response["products"][0]["category"] == "smartphones"
        ), f'Expected {response["products"][0]["category"]} to be string "smartphones", but it is not.'
        assert (
            response["products"][0]["thumbnail"]
            == "https://cdn.dummyjson.com/product-images/1/thumbnail.jpg"
        ), f'Expected {response["products"][0]["thumbnail"]} to be string "https://cdn.dummyjson.com/product-images/1/thumbnail.jpg", but it is not.'
        assert isinstance(
            response["products"][0]["images"], list
        ), "Expected the object tobe a list, but it's not"
        assert (
            len(response["products"][0]["images"]) == 5
        ), "Expected the list to have length 5, but it's not"
        assert (
            response["products"][0]["images"][0]
            == "https://cdn.dummyjson.com/product-images/1/1.jpg"
        ), f'Expected {response["products"][0]["images"][0]} to be string "https://cdn.dummyjson.com/product-images/1/1.jpg", but it is not.'
        assert (
            response["products"][0]["images"][1]
            == "https://cdn.dummyjson.com/product-images/1/2.jpg"
        ), f'Expected {response["products"][0]["images"][1]} to be string "https://cdn.dummyjson.com/product-images/1/2.jpg", but it is not.'
        assert (
            response["products"][0]["images"][2]
            == "https://cdn.dummyjson.com/product-images/1/3.jpg"
        ), f'Expected {response["products"][0]["images"][2]} to be string "https://cdn.dummyjson.com/product-images/1/3.jpg", but it is not.'
        assert (
            response["products"][0]["images"][3]
            == "https://cdn.dummyjson.com/product-images/1/4.jpg"
        ), f'Expected {response["products"][0]["images"][3]} to be string "https://cdn.dummyjson.com/product-images/1/4.jpg", but it is not.'
        assert (
            response["products"][0]["images"][4]
            == "https://cdn.dummyjson.com/product-images/1/thumbnail.jpg"
        ), f'Expected {response["products"][0]["images"][4]} to be string "https://cdn.dummyjson.com/product-images/1/thumbnail.jpg", but it is not.'
        keys_to_assert = [
            "id",
            "title",
            "description",
            "price",
            "discountPercentage",
            "rating",
            "stock",
            "brand",
            "category",
            "thumbnail",
            "images",
        ]
        for key in keys_to_assert:
            assert (
                key in response["products"][1]
            ), f"Expected {key} to be in the dictionary, but it's not."
        assert (
            response["products"][1]["id"] == 2
        ), f'Expected {response["products"][1]["id"]} to be number 2, but it is not.'
        assert (
            response["products"][1]["title"] == "iPhone X"
        ), f'Expected {response["products"][1]["title"]} to be string "iPhone X", but it is not.'
        assert (
            response["products"][1]["description"]
            == "SIM-Free, Model A19211 6.5-inch Super Retina HD display with OLED technology A12 Bionic chip with ..."
        ), f'Expected {response["products"][1]["description"]} to be string "SIM-Free, Model A19211 6.5-inch Super Retina HD display with OLED technology A12 Bionic chip with ...", but it is not.'
        assert (
            response["products"][1]["price"] == 899
        ), f'Expected {response["products"][1]["price"]} to be number 899, but it is not.'
        assert (
            response["products"][1]["discountPercentage"] == 17.94
        ), f'Expected {response["products"][1]["discountPercentage"]} to be number 17.94, but it is not.'
        assert (
            response["products"][1]["rating"] == 4.44
        ), f'Expected {response["products"][1]["rating"]} to be number 4.44, but it is not.'
        assert (
            response["products"][1]["stock"] == 34
        ), f'Expected {response["products"][1]["stock"]} to be number 34, but it is not.'
        assert (
            response["products"][1]["brand"] == "Apple"
        ), f'Expected {response["products"][1]["brand"]} to be string "Apple", but it is not.'
        assert (
            response["products"][1]["category"] == "smartphones"
        ), f'Expected {response["products"][1]["category"]} to be string "smartphones", but it is not.'
        assert (
            response["products"][1]["thumbnail"]
            == "https://cdn.dummyjson.com/product-images/2/thumbnail.jpg"
        ), f'Expected {response["products"][1]["thumbnail"]} to be string "https://cdn.dummyjson.com/product-images/2/thumbnail.jpg", but it is not.'
        assert isinstance(
            response["products"][1]["images"], list
        ), "Expected the object tobe a list, but it's not"
        assert (
            len(response["products"][1]["images"]) == 4
        ), "Expected the list to have length 4, but it's not"
        assert (
            response["products"][1]["images"][0]
            == "https://cdn.dummyjson.com/product-images/2/1.jpg"
        ), f'Expected {response["products"][1]["images"][0]} to be string "https://cdn.dummyjson.com/product-images/2/1.jpg", but it is not.'
        assert (
            response["products"][1]["images"][1]
            == "https://cdn.dummyjson.com/product-images/2/2.jpg"
        ), f'Expected {response["products"][1]["images"][1]} to be string "https://cdn.dummyjson.com/product-images/2/2.jpg", but it is not.'
        assert (
            response["products"][1]["images"][2]
            == "https://cdn.dummyjson.com/product-images/2/3.jpg"
        ), f'Expected {response["products"][1]["images"][2]} to be string "https://cdn.dummyjson.com/product-images/2/3.jpg", but it is not.'
        assert (
            response["products"][1]["images"][3]
            == "https://cdn.dummyjson.com/product-images/2/thumbnail.jpg"
        ), f'Expected {response["products"][1]["images"][3]} to be string "https://cdn.dummyjson.com/product-images/2/thumbnail.jpg", but it is not.'
        keys_to_assert = [
            "id",
            "title",
            "description",
            "price",
            "discountPercentage",
            "rating",
            "stock",
            "brand",
            "category",
            "thumbnail",
            "images",
        ]
        for key in keys_to_assert:
            assert (
                key in response["products"][2]
            ), f"Expected {key} to be in the dictionary, but it's not."
        assert (
            response["products"][2]["id"] == 3
        ), f'Expected {response["products"][2]["id"]} to be number 3, but it is not.'
        assert (
            response["products"][2]["title"] == "Samsung Universe 9"
        ), f'Expected {response["products"][2]["title"]} to be string "Samsung Universe 9", but it is not.'
        assert (
            response["products"][2]["description"]
            == "Samsung's new variant which goes beyond Galaxy to the Universe"
        ), f'Expected {response["products"][2]["description"]} to be string "Samsung\'s new variant which goes beyond Galaxy to the Universe", but it is not.'
        assert (
            response["products"][2]["price"] == 1249
        ), f'Expected {response["products"][2]["price"]} to be number 1249, but it is not.'
        assert (
            response["products"][2]["discountPercentage"] == 15.46
        ), f'Expected {response["products"][2]["discountPercentage"]} to be number 15.46, but it is not.'
        assert (
            response["products"][2]["rating"] == 4.09
        ), f'Expected {response["products"][2]["rating"]} to be number 4.09, but it is not.'
        assert (
            response["products"][2]["stock"] == 36
        ), f'Expected {response["products"][2]["stock"]} to be number 36, but it is not.'
        assert (
            response["products"][2]["brand"] == "Samsung"
        ), f'Expected {response["products"][2]["brand"]} to be string "Samsung", but it is not.'
        assert (
            response["products"][2]["category"] == "smartphones"
        ), f'Expected {response["products"][2]["category"]} to be string "smartphones", but it is not.'
        assert (
            response["products"][2]["thumbnail"]
            == "https://cdn.dummyjson.com/product-images/3/thumbnail.jpg"
        ), f'Expected {response["products"][2]["thumbnail"]} to be string "https://cdn.dummyjson.com/product-images/3/thumbnail.jpg", but it is not.'
        assert isinstance(
            response["products"][2]["images"], list
        ), "Expected the object tobe a list, but it's not"
        assert (
            len(response["products"][2]["images"]) == 1
        ), "Expected the list to have length 1, but it's not"
        assert (
            response["products"][2]["images"][0]
            == "https://cdn.dummyjson.com/product-images/3/1.jpg"
        ), f'Expected {response["products"][2]["images"][0]} to be string "https://cdn.dummyjson.com/product-images/3/1.jpg", but it is not.'
        keys_to_assert = [
            "id",
            "title",
            "description",
            "price",
            "discountPercentage",
            "rating",
            "stock",
            "brand",
            "category",
            "thumbnail",
            "images",
        ]
        for key in keys_to_assert:
            assert (
                key in response["products"][3]
            ), f"Expected {key} to be in the dictionary, but it's not."
        assert (
            response["products"][3]["id"] == 4
        ), f'Expected {response["products"][3]["id"]} to be number 4, but it is not.'
        assert (
            response["products"][3]["title"] == "OPPOF19"
        ), f'Expected {response["products"][3]["title"]} to be string "OPPOF19", but it is not.'
        assert (
            response["products"][3]["description"]
            == "OPPO F19 is officially announced on April 2021."
        ), f'Expected {response["products"][3]["description"]} to be string "OPPO F19 is officially announced on April 2021.", but it is not.'
        assert (
            response["products"][3]["price"] == 280
        ), f'Expected {response["products"][3]["price"]} to be number 280, but it is not.'
        assert (
            response["products"][3]["discountPercentage"] == 17.91
        ), f'Expected {response["products"][3]["discountPercentage"]} to be number 17.91, but it is not.'
        assert (
            response["products"][3]["rating"] == 4.3
        ), f'Expected {response["products"][3]["rating"]} to be number 4.3, but it is not.'
        assert (
            response["products"][3]["stock"] == 123
        ), f'Expected {response["products"][3]["stock"]} to be number 123, but it is not.'
        assert (
            response["products"][3]["brand"] == "OPPO"
        ), f'Expected {response["products"][3]["brand"]} to be string "OPPO", but it is not.'
        assert (
            response["products"][3]["category"] == "smartphones"
        ), f'Expected {response["products"][3]["category"]} to be string "smartphones", but it is not.'
        assert (
            response["products"][3]["thumbnail"]
            == "https://cdn.dummyjson.com/product-images/4/thumbnail.jpg"
        ), f'Expected {response["products"][3]["thumbnail"]} to be string "https://cdn.dummyjson.com/product-images/4/thumbnail.jpg", but it is not.'
        assert isinstance(
            response["products"][3]["images"], list
        ), "Expected the object tobe a list, but it's not"
        assert (
            len(response["products"][3]["images"]) == 5
        ), "Expected the list to have length 5, but it's not"
        assert (
            response["products"][3]["images"][0]
            == "https://cdn.dummyjson.com/product-images/4/1.jpg"
        ), f'Expected {response["products"][3]["images"][0]} to be string "https://cdn.dummyjson.com/product-images/4/1.jpg", but it is not.'
        assert (
            response["products"][3]["images"][1]
            == "https://cdn.dummyjson.com/product-images/4/2.jpg"
        ), f'Expected {response["products"][3]["images"][1]} to be string "https://cdn.dummyjson.com/product-images/4/2.jpg", but it is not.'
        assert (
            response["products"][3]["images"][2]
            == "https://cdn.dummyjson.com/product-images/4/3.jpg"
        ), f'Expected {response["products"][3]["images"][2]} to be string "https://cdn.dummyjson.com/product-images/4/3.jpg", but it is not.'
        assert (
            response["products"][3]["images"][3]
            == "https://cdn.dummyjson.com/product-images/4/4.jpg"
        ), f'Expected {response["products"][3]["images"][3]} to be string "https://cdn.dummyjson.com/product-images/4/4.jpg", but it is not.'
        assert (
            response["products"][3]["images"][4]
            == "https://cdn.dummyjson.com/product-images/4/thumbnail.jpg"
        ), f'Expected {response["products"][3]["images"][4]} to be string "https://cdn.dummyjson.com/product-images/4/thumbnail.jpg", but it is not.'
        keys_to_assert = [
            "id",
            "title",
            "description",
            "price",
            "discountPercentage",
            "rating",
            "stock",
            "brand",
            "category",
            "thumbnail",
            "images",
        ]
        for key in keys_to_assert:
            assert (
                key in response["products"][4]
            ), f"Expected {key} to be in the dictionary, but it's not."
        assert (
            response["products"][4]["id"] == 5
        ), f'Expected {response["products"][4]["id"]} to be number 5, but it is not.'
        assert (
            response["products"][4]["title"] == "Huawei P30"
        ), f'Expected {response["products"][4]["title"]} to be string "Huawei P30", but it is not.'
        assert (
            response["products"][4]["description"]
            == "Huawei’s re-badged P30 Pro New Edition was officially unveiled yesterday in Germany and now the device has made its way to the UK."
        ), f'Expected {response["products"][4]["description"]} to be string "Huawei’s re-badged P30 Pro New Edition was officially unveiled yesterday in Germany and now the device has made its way to the UK.", but it is not.'
        assert (
            response["products"][4]["price"] == 499
        ), f'Expected {response["products"][4]["price"]} to be number 499, but it is not.'
        assert (
            response["products"][4]["discountPercentage"] == 10.58
        ), f'Expected {response["products"][4]["discountPercentage"]} to be number 10.58, but it is not.'
        assert (
            response["products"][4]["rating"] == 4.09
        ), f'Expected {response["products"][4]["rating"]} to be number 4.09, but it is not.'
        assert (
            response["products"][4]["stock"] == 32
        ), f'Expected {response["products"][4]["stock"]} to be number 32, but it is not.'
        assert (
            response["products"][4]["brand"] == "Huawei"
        ), f'Expected {response["products"][4]["brand"]} to be string "Huawei", but it is not.'
        assert (
            response["products"][4]["category"] == "smartphones"
        ), f'Expected {response["products"][4]["category"]} to be string "smartphones", but it is not.'
        assert (
            response["products"][4]["thumbnail"]
            == "https://cdn.dummyjson.com/product-images/5/thumbnail.jpg"
        ), f'Expected {response["products"][4]["thumbnail"]} to be string "https://cdn.dummyjson.com/product-images/5/thumbnail.jpg", but it is not.'
        assert isinstance(
            response["products"][4]["images"], list
        ), "Expected the object tobe a list, but it's not"
        assert (
            len(response["products"][4]["images"]) == 3
        ), "Expected the list to have length 3, but it's not"
        assert (
            response["products"][4]["images"][0]
            == "https://cdn.dummyjson.com/product-images/5/1.jpg"
        ), f'Expected {response["products"][4]["images"][0]} to be string "https://cdn.dummyjson.com/product-images/5/1.jpg", but it is not.'
        assert (
            response["products"][4]["images"][1]
            == "https://cdn.dummyjson.com/product-images/5/2.jpg"
        ), f'Expected {response["products"][4]["images"][1]} to be string "https://cdn.dummyjson.com/product-images/5/2.jpg", but it is not.'
        assert (
            response["products"][4]["images"][2]
            == "https://cdn.dummyjson.com/product-images/5/3.jpg"
        ), f'Expected {response["products"][4]["images"][2]} to be string "https://cdn.dummyjson.com/product-images/5/3.jpg", but it is not.'
        keys_to_assert = [
            "id",
            "title",
            "description",
            "price",
            "discountPercentage",
            "rating",
            "stock",
            "brand",
            "category",
            "thumbnail",
            "images",
        ]
        for key in keys_to_assert:
            assert (
                key in response["products"][5]
            ), f"Expected {key} to be in the dictionary, but it's not."
        assert (
            response["products"][5]["id"] == 6
        ), f'Expected {response["products"][5]["id"]} to be number 6, but it is not.'
        assert (
            response["products"][5]["title"] == "MacBook Pro"
        ), f'Expected {response["products"][5]["title"]} to be string "MacBook Pro", but it is not.'
        assert (
            response["products"][5]["description"]
            == "MacBook Pro 2021 with mini-LED display may launch between September, November"
        ), f'Expected {response["products"][5]["description"]} to be string "MacBook Pro 2021 with mini-LED display may launch between September, November", but it is not.'
        assert (
            response["products"][5]["price"] == 1749
        ), f'Expected {response["products"][5]["price"]} to be number 1749, but it is not.'
        assert (
            response["products"][5]["discountPercentage"] == 11.02
        ), f'Expected {response["products"][5]["discountPercentage"]} to be number 11.02, but it is not.'
        assert (
            response["products"][5]["rating"] == 4.57
        ), f'Expected {response["products"][5]["rating"]} to be number 4.57, but it is not.'
        assert (
            response["products"][5]["stock"] == 83
        ), f'Expected {response["products"][5]["stock"]} to be number 83, but it is not.'
        assert (
            response["products"][5]["brand"] == "Apple"
        ), f'Expected {response["products"][5]["brand"]} to be string "Apple", but it is not.'
        assert (
            response["products"][5]["category"] == "laptops"
        ), f'Expected {response["products"][5]["category"]} to be string "laptops", but it is not.'
        assert (
            response["products"][5]["thumbnail"]
            == "https://cdn.dummyjson.com/product-images/6/thumbnail.png"
        ), f'Expected {response["products"][5]["thumbnail"]} to be string "https://cdn.dummyjson.com/product-images/6/thumbnail.png", but it is not.'
        assert isinstance(
            response["products"][5]["images"], list
        ), "Expected the object tobe a list, but it's not"
        assert (
            len(response["products"][5]["images"]) == 4
        ), "Expected the list to have length 4, but it's not"
        assert (
            response["products"][5]["images"][0]
            == "https://cdn.dummyjson.com/product-images/6/1.png"
        ), f'Expected {response["products"][5]["images"][0]} to be string "https://cdn.dummyjson.com/product-images/6/1.png", but it is not.'
        assert (
            response["products"][5]["images"][1]
            == "https://cdn.dummyjson.com/product-images/6/2.jpg"
        ), f'Expected {response["products"][5]["images"][1]} to be string "https://cdn.dummyjson.com/product-images/6/2.jpg", but it is not.'
        assert (
            response["products"][5]["images"][2]
            == "https://cdn.dummyjson.com/product-images/6/3.png"
        ), f'Expected {response["products"][5]["images"][2]} to be string "https://cdn.dummyjson.com/product-images/6/3.png", but it is not.'
        assert (
            response["products"][5]["images"][3]
            == "https://cdn.dummyjson.com/product-images/6/4.jpg"
        ), f'Expected {response["products"][5]["images"][3]} to be string "https://cdn.dummyjson.com/product-images/6/4.jpg", but it is not.'
        keys_to_assert = [
            "id",
            "title",
            "description",
            "price",
            "discountPercentage",
            "rating",
            "stock",
            "brand",
            "category",
            "thumbnail",
            "images",
        ]
        for key in keys_to_assert:
            assert (
                key in response["products"][6]
            ), f"Expected {key} to be in the dictionary, but it's not."
        assert (
            response["products"][6]["id"] == 7
        ), f'Expected {response["products"][6]["id"]} to be number 7, but it is not.'
        assert (
            response["products"][6]["title"] == "Samsung Galaxy Book"
        ), f'Expected {response["products"][6]["title"]} to be string "Samsung Galaxy Book", but it is not.'
        assert (
            response["products"][6]["description"]
            == "Samsung Galaxy Book S (2020) Laptop With Intel Lakefield Chip, 8GB of RAM Launched"
        ), f'Expected {response["products"][6]["description"]} to be string "Samsung Galaxy Book S (2020) Laptop With Intel Lakefield Chip, 8GB of RAM Launched", but it is not.'
        assert (
            response["products"][6]["price"] == 1499
        ), f'Expected {response["products"][6]["price"]} to be number 1499, but it is not.'
        assert (
            response["products"][6]["discountPercentage"] == 4.15
        ), f'Expected {response["products"][6]["discountPercentage"]} to be number 4.15, but it is not.'
        assert (
            response["products"][6]["rating"] == 4.25
        ), f'Expected {response["products"][6]["rating"]} to be number 4.25, but it is not.'
        assert (
            response["products"][6]["stock"] == 50
        ), f'Expected {response["products"][6]["stock"]} to be number 50, but it is not.'
        assert (
            response["products"][6]["brand"] == "Samsung"
        ), f'Expected {response["products"][6]["brand"]} to be string "Samsung", but it is not.'
        assert (
            response["products"][6]["category"] == "laptops"
        ), f'Expected {response["products"][6]["category"]} to be string "laptops", but it is not.'
        assert (
            response["products"][6]["thumbnail"]
            == "https://cdn.dummyjson.com/product-images/7/thumbnail.jpg"
        ), f'Expected {response["products"][6]["thumbnail"]} to be string "https://cdn.dummyjson.com/product-images/7/thumbnail.jpg", but it is not.'
        assert isinstance(
            response["products"][6]["images"], list
        ), "Expected the object tobe a list, but it's not"
        assert (
            len(response["products"][6]["images"]) == 4
        ), "Expected the list to have length 4, but it's not"
        assert (
            response["products"][6]["images"][0]
            == "https://cdn.dummyjson.com/product-images/7/1.jpg"
        ), f'Expected {response["products"][6]["images"][0]} to be string "https://cdn.dummyjson.com/product-images/7/1.jpg", but it is not.'
        assert (
            response["products"][6]["images"][1]
            == "https://cdn.dummyjson.com/product-images/7/2.jpg"
        ), f'Expected {response["products"][6]["images"][1]} to be string "https://cdn.dummyjson.com/product-images/7/2.jpg", but it is not.'
        assert (
            response["products"][6]["images"][2]
            == "https://cdn.dummyjson.com/product-images/7/3.jpg"
        ), f'Expected {response["products"][6]["images"][2]} to be string "https://cdn.dummyjson.com/product-images/7/3.jpg", but it is not.'
        assert (
            response["products"][6]["images"][3]
            == "https://cdn.dummyjson.com/product-images/7/thumbnail.jpg"
        ), f'Expected {response["products"][6]["images"][3]} to be string "https://cdn.dummyjson.com/product-images/7/thumbnail.jpg", but it is not.'
        keys_to_assert = [
            "id",
            "title",
            "description",
            "price",
            "discountPercentage",
            "rating",
            "stock",
            "brand",
            "category",
            "thumbnail",
            "images",
        ]
        for key in keys_to_assert:
            assert (
                key in response["products"][7]
            ), f"Expected {key} to be in the dictionary, but it's not."
        assert (
            response["products"][7]["id"] == 8
        ), f'Expected {response["products"][7]["id"]} to be number 8, but it is not.'
        assert (
            response["products"][7]["title"] == "Microsoft Surface Laptop 4"
        ), f'Expected {response["products"][7]["title"]} to be string "Microsoft Surface Laptop 4", but it is not.'
        assert (
            response["products"][7]["description"]
            == "Style and speed. Stand out on HD video calls backed by Studio Mics. Capture ideas on the vibrant touchscreen."
        ), f'Expected {response["products"][7]["description"]} to be string "Style and speed. Stand out on HD video calls backed by Studio Mics. Capture ideas on the vibrant touchscreen.", but it is not.'
        assert (
            response["products"][7]["price"] == 1499
        ), f'Expected {response["products"][7]["price"]} to be number 1499, but it is not.'
        assert (
            response["products"][7]["discountPercentage"] == 10.23
        ), f'Expected {response["products"][7]["discountPercentage"]} to be number 10.23, but it is not.'
        assert (
            response["products"][7]["rating"] == 4.43
        ), f'Expected {response["products"][7]["rating"]} to be number 4.43, but it is not.'
        assert (
            response["products"][7]["stock"] == 68
        ), f'Expected {response["products"][7]["stock"]} to be number 68, but it is not.'
        assert (
            response["products"][7]["brand"] == "Microsoft Surface"
        ), f'Expected {response["products"][7]["brand"]} to be string "Microsoft Surface", but it is not.'
        assert (
            response["products"][7]["category"] == "laptops"
        ), f'Expected {response["products"][7]["category"]} to be string "laptops", but it is not.'
        assert (
            response["products"][7]["thumbnail"]
            == "https://cdn.dummyjson.com/product-images/8/thumbnail.jpg"
        ), f'Expected {response["products"][7]["thumbnail"]} to be string "https://cdn.dummyjson.com/product-images/8/thumbnail.jpg", but it is not.'
        assert isinstance(
            response["products"][7]["images"], list
        ), "Expected the object tobe a list, but it's not"
        assert (
            len(response["products"][7]["images"]) == 5
        ), "Expected the list to have length 5, but it's not"
        assert (
            response["products"][7]["images"][0]
            == "https://cdn.dummyjson.com/product-images/8/1.jpg"
        ), f'Expected {response["products"][7]["images"][0]} to be string "https://cdn.dummyjson.com/product-images/8/1.jpg", but it is not.'
        assert (
            response["products"][7]["images"][1]
            == "https://cdn.dummyjson.com/product-images/8/2.jpg"
        ), f'Expected {response["products"][7]["images"][1]} to be string "https://cdn.dummyjson.com/product-images/8/2.jpg", but it is not.'
        assert (
            response["products"][7]["images"][2]
            == "https://cdn.dummyjson.com/product-images/8/3.jpg"
        ), f'Expected {response["products"][7]["images"][2]} to be string "https://cdn.dummyjson.com/product-images/8/3.jpg", but it is not.'
        assert (
            response["products"][7]["images"][3]
            == "https://cdn.dummyjson.com/product-images/8/4.jpg"
        ), f'Expected {response["products"][7]["images"][3]} to be string "https://cdn.dummyjson.com/product-images/8/4.jpg", but it is not.'
        assert (
            response["products"][7]["images"][4]
            == "https://cdn.dummyjson.com/product-images/8/thumbnail.jpg"
        ), f'Expected {response["products"][7]["images"][4]} to be string "https://cdn.dummyjson.com/product-images/8/thumbnail.jpg", but it is not.'
        keys_to_assert = [
            "id",
            "title",
            "description",
            "price",
            "discountPercentage",
            "rating",
            "stock",
            "brand",
            "category",
            "thumbnail",
            "images",
        ]
        for key in keys_to_assert:
            assert (
                key in response["products"][8]
            ), f"Expected {key} to be in the dictionary, but it's not."
        assert (
            response["products"][8]["id"] == 9
        ), f'Expected {response["products"][8]["id"]} to be number 9, but it is not.'
        assert (
            response["products"][8]["title"] == "Infinix INBOOK"
        ), f'Expected {response["products"][8]["title"]} to be string "Infinix INBOOK", but it is not.'
        assert (
            response["products"][8]["description"]
            == "Infinix Inbook X1 Ci3 10th 8GB 256GB 14 Win10 Grey – 1 Year Warranty"
        ), f'Expected {response["products"][8]["description"]} to be string "Infinix Inbook X1 Ci3 10th 8GB 256GB 14 Win10 Grey – 1 Year Warranty", but it is not.'
        assert (
            response["products"][8]["price"] == 1099
        ), f'Expected {response["products"][8]["price"]} to be number 1099, but it is not.'
        assert (
            response["products"][8]["discountPercentage"] == 11.83
        ), f'Expected {response["products"][8]["discountPercentage"]} to be number 11.83, but it is not.'
        assert (
            response["products"][8]["rating"] == 4.54
        ), f'Expected {response["products"][8]["rating"]} to be number 4.54, but it is not.'
        assert (
            response["products"][8]["stock"] == 96
        ), f'Expected {response["products"][8]["stock"]} to be number 96, but it is not.'
        assert (
            response["products"][8]["brand"] == "Infinix"
        ), f'Expected {response["products"][8]["brand"]} to be string "Infinix", but it is not.'
        assert (
            response["products"][8]["category"] == "laptops"
        ), f'Expected {response["products"][8]["category"]} to be string "laptops", but it is not.'
        assert (
            response["products"][8]["thumbnail"]
            == "https://cdn.dummyjson.com/product-images/9/thumbnail.jpg"
        ), f'Expected {response["products"][8]["thumbnail"]} to be string "https://cdn.dummyjson.com/product-images/9/thumbnail.jpg", but it is not.'
        assert isinstance(
            response["products"][8]["images"], list
        ), "Expected the object tobe a list, but it's not"
        assert (
            len(response["products"][8]["images"]) == 5
        ), "Expected the list to have length 5, but it's not"
        assert (
            response["products"][8]["images"][0]
            == "https://cdn.dummyjson.com/product-images/9/1.jpg"
        ), f'Expected {response["products"][8]["images"][0]} to be string "https://cdn.dummyjson.com/product-images/9/1.jpg", but it is not.'
        assert (
            response["products"][8]["images"][1]
            == "https://cdn.dummyjson.com/product-images/9/2.png"
        ), f'Expected {response["products"][8]["images"][1]} to be string "https://cdn.dummyjson.com/product-images/9/2.png", but it is not.'
        assert (
            response["products"][8]["images"][2]
            == "https://cdn.dummyjson.com/product-images/9/3.png"
        ), f'Expected {response["products"][8]["images"][2]} to be string "https://cdn.dummyjson.com/product-images/9/3.png", but it is not.'
        assert (
            response["products"][8]["images"][3]
            == "https://cdn.dummyjson.com/product-images/9/4.jpg"
        ), f'Expected {response["products"][8]["images"][3]} to be string "https://cdn.dummyjson.com/product-images/9/4.jpg", but it is not.'
        assert (
            response["products"][8]["images"][4]
            == "https://cdn.dummyjson.com/product-images/9/thumbnail.jpg"
        ), f'Expected {response["products"][8]["images"][4]} to be string "https://cdn.dummyjson.com/product-images/9/thumbnail.jpg", but it is not.'
        keys_to_assert = [
            "id",
            "title",
            "description",
            "price",
            "discountPercentage",
            "rating",
            "stock",
            "brand",
            "category",
            "thumbnail",
            "images",
        ]
        for key in keys_to_assert:
            assert (
                key in response["products"][9]
            ), f"Expected {key} to be in the dictionary, but it's not."
        assert (
            response["products"][9]["id"] == 10
        ), f'Expected {response["products"][9]["id"]} to be number 10, but it is not.'
        assert (
            response["products"][9]["title"] == "HP Pavilion 15-DK1056WM"
        ), f'Expected {response["products"][9]["title"]} to be string "HP Pavilion 15-DK1056WM", but it is not.'
        assert (
            response["products"][9]["description"]
            == "HP Pavilion 15-DK1056WM Gaming Laptop 10th Gen Core i5, 8GB, 256GB SSD, GTX 1650 4GB, Windows 10"
        ), f'Expected {response["products"][9]["description"]} to be string "HP Pavilion 15-DK1056WM Gaming Laptop 10th Gen Core i5, 8GB, 256GB SSD, GTX 1650 4GB, Windows 10", but it is not.'
        assert (
            response["products"][9]["price"] == 1099
        ), f'Expected {response["products"][9]["price"]} to be number 1099, but it is not.'
        assert (
            response["products"][9]["discountPercentage"] == 6.18
        ), f'Expected {response["products"][9]["discountPercentage"]} to be number 6.18, but it is not.'
        assert (
            response["products"][9]["rating"] == 4.43
        ), f'Expected {response["products"][9]["rating"]} to be number 4.43, but it is not.'
        assert (
            response["products"][9]["stock"] == 89
        ), f'Expected {response["products"][9]["stock"]} to be number 89, but it is not.'
        assert (
            response["products"][9]["brand"] == "HP Pavilion"
        ), f'Expected {response["products"][9]["brand"]} to be string "HP Pavilion", but it is not.'
        assert (
            response["products"][9]["category"] == "laptops"
        ), f'Expected {response["products"][9]["category"]} to be string "laptops", but it is not.'
        assert (
            response["products"][9]["thumbnail"]
            == "https://cdn.dummyjson.com/product-images/10/thumbnail.jpeg"
        ), f'Expected {response["products"][9]["thumbnail"]} to be string "https://cdn.dummyjson.com/product-images/10/thumbnail.jpeg", but it is not.'
        assert isinstance(
            response["products"][9]["images"], list
        ), "Expected the object tobe a list, but it's not"
        assert (
            len(response["products"][9]["images"]) == 4
        ), "Expected the list to have length 4, but it's not"
        assert (
            response["products"][9]["images"][0]
            == "https://cdn.dummyjson.com/product-images/10/1.jpg"
        ), f'Expected {response["products"][9]["images"][0]} to be string "https://cdn.dummyjson.com/product-images/10/1.jpg", but it is not.'
        assert (
            response["products"][9]["images"][1]
            == "https://cdn.dummyjson.com/product-images/10/2.jpg"
        ), f'Expected {response["products"][9]["images"][1]} to be string "https://cdn.dummyjson.com/product-images/10/2.jpg", but it is not.'
        assert (
            response["products"][9]["images"][2]
            == "https://cdn.dummyjson.com/product-images/10/3.jpg"
        ), f'Expected {response["products"][9]["images"][2]} to be string "https://cdn.dummyjson.com/product-images/10/3.jpg", but it is not.'
        assert (
            response["products"][9]["images"][3]
            == "https://cdn.dummyjson.com/product-images/10/thumbnail.jpeg"
        ), f'Expected {response["products"][9]["images"][3]} to be string "https://cdn.dummyjson.com/product-images/10/thumbnail.jpeg", but it is not.'
        keys_to_assert = [
            "id",
            "title",
            "description",
            "price",
            "discountPercentage",
            "rating",
            "stock",
            "brand",
            "category",
            "thumbnail",
            "images",
        ]
        for key in keys_to_assert:
            assert (
                key in response["products"][10]
            ), f"Expected {key} to be in the dictionary, but it's not."
        assert (
            response["products"][10]["id"] == 11
        ), f'Expected {response["products"][10]["id"]} to be number 11, but it is not.'
        assert (
            response["products"][10]["title"] == "perfume Oil"
        ), f'Expected {response["products"][10]["title"]} to be string "perfume Oil", but it is not.'
        assert (
            response["products"][10]["description"]
            == "Mega Discount, Impression of Acqua Di Gio by GiorgioArmani concentrated attar perfume Oil"
        ), f'Expected {response["products"][10]["description"]} to be string "Mega Discount, Impression of Acqua Di Gio by GiorgioArmani concentrated attar perfume Oil", but it is not.'
        assert (
            response["products"][10]["price"] == 13
        ), f'Expected {response["products"][10]["price"]} to be number 13, but it is not.'
        assert (
            response["products"][10]["discountPercentage"] == 8.4
        ), f'Expected {response["products"][10]["discountPercentage"]} to be number 8.4, but it is not.'
        assert (
            response["products"][10]["rating"] == 4.26
        ), f'Expected {response["products"][10]["rating"]} to be number 4.26, but it is not.'
        assert (
            response["products"][10]["stock"] == 65
        ), f'Expected {response["products"][10]["stock"]} to be number 65, but it is not.'
        assert (
            response["products"][10]["brand"] == "Impression of Acqua Di Gio"
        ), f'Expected {response["products"][10]["brand"]} to be string "Impression of Acqua Di Gio", but it is not.'
        assert (
            response["products"][10]["category"] == "fragrances"
        ), f'Expected {response["products"][10]["category"]} to be string "fragrances", but it is not.'
        assert (
            response["products"][10]["thumbnail"]
            == "https://cdn.dummyjson.com/product-images/11/thumbnail.jpg"
        ), f'Expected {response["products"][10]["thumbnail"]} to be string "https://cdn.dummyjson.com/product-images/11/thumbnail.jpg", but it is not.'
        assert isinstance(
            response["products"][10]["images"], list
        ), "Expected the object tobe a list, but it's not"
        assert (
            len(response["products"][10]["images"]) == 4
        ), "Expected the list to have length 4, but it's not"
        assert (
            response["products"][10]["images"][0]
            == "https://cdn.dummyjson.com/product-images/11/1.jpg"
        ), f'Expected {response["products"][10]["images"][0]} to be string "https://cdn.dummyjson.com/product-images/11/1.jpg", but it is not.'
        assert (
            response["products"][10]["images"][1]
            == "https://cdn.dummyjson.com/product-images/11/2.jpg"
        ), f'Expected {response["products"][10]["images"][1]} to be string "https://cdn.dummyjson.com/product-images/11/2.jpg", but it is not.'
        assert (
            response["products"][10]["images"][2]
            == "https://cdn.dummyjson.com/product-images/11/3.jpg"
        ), f'Expected {response["products"][10]["images"][2]} to be string "https://cdn.dummyjson.com/product-images/11/3.jpg", but it is not.'
        assert (
            response["products"][10]["images"][3]
            == "https://cdn.dummyjson.com/product-images/11/thumbnail.jpg"
        ), f'Expected {response["products"][10]["images"][3]} to be string "https://cdn.dummyjson.com/product-images/11/thumbnail.jpg", but it is not.'
        keys_to_assert = [
            "id",
            "title",
            "description",
            "price",
            "discountPercentage",
            "rating",
            "stock",
            "brand",
            "category",
            "thumbnail",
            "images",
        ]
        for key in keys_to_assert:
            assert (
                key in response["products"][11]
            ), f"Expected {key} to be in the dictionary, but it's not."
        assert (
            response["products"][11]["id"] == 12
        ), f'Expected {response["products"][11]["id"]} to be number 12, but it is not.'
        assert (
            response["products"][11]["title"] == "Brown Perfume"
        ), f'Expected {response["products"][11]["title"]} to be string "Brown Perfume", but it is not.'
        assert (
            response["products"][11]["description"]
            == "Royal_Mirage Sport Brown Perfume for Men & Women - 120ml"
        ), f'Expected {response["products"][11]["description"]} to be string "Royal_Mirage Sport Brown Perfume for Men & Women - 120ml", but it is not.'
        assert (
            response["products"][11]["price"] == 40
        ), f'Expected {response["products"][11]["price"]} to be number 40, but it is not.'
        assert (
            response["products"][11]["discountPercentage"] == 15.66
        ), f'Expected {response["products"][11]["discountPercentage"]} to be number 15.66, but it is not.'
        assert (
            response["products"][11]["rating"] == 4
        ), f'Expected {response["products"][11]["rating"]} to be number 4, but it is not.'
        assert (
            response["products"][11]["stock"] == 52
        ), f'Expected {response["products"][11]["stock"]} to be number 52, but it is not.'
        assert (
            response["products"][11]["brand"] == "Royal_Mirage"
        ), f'Expected {response["products"][11]["brand"]} to be string "Royal_Mirage", but it is not.'
        assert (
            response["products"][11]["category"] == "fragrances"
        ), f'Expected {response["products"][11]["category"]} to be string "fragrances", but it is not.'
        assert (
            response["products"][11]["thumbnail"]
            == "https://cdn.dummyjson.com/product-images/12/thumbnail.jpg"
        ), f'Expected {response["products"][11]["thumbnail"]} to be string "https://cdn.dummyjson.com/product-images/12/thumbnail.jpg", but it is not.'
        assert isinstance(
            response["products"][11]["images"], list
        ), "Expected the object tobe a list, but it's not"
        assert (
            len(response["products"][11]["images"]) == 5
        ), "Expected the list to have length 5, but it's not"
        assert (
            response["products"][11]["images"][0]
            == "https://cdn.dummyjson.com/product-images/12/1.jpg"
        ), f'Expected {response["products"][11]["images"][0]} to be string "https://cdn.dummyjson.com/product-images/12/1.jpg", but it is not.'
        assert (
            response["products"][11]["images"][1]
            == "https://cdn.dummyjson.com/product-images/12/2.jpg"
        ), f'Expected {response["products"][11]["images"][1]} to be string "https://cdn.dummyjson.com/product-images/12/2.jpg", but it is not.'
        assert (
            response["products"][11]["images"][2]
            == "https://cdn.dummyjson.com/product-images/12/3.png"
        ), f'Expected {response["products"][11]["images"][2]} to be string "https://cdn.dummyjson.com/product-images/12/3.png", but it is not.'
        assert (
            response["products"][11]["images"][3]
            == "https://cdn.dummyjson.com/product-images/12/4.jpg"
        ), f'Expected {response["products"][11]["images"][3]} to be string "https://cdn.dummyjson.com/product-images/12/4.jpg", but it is not.'
        assert (
            response["products"][11]["images"][4]
            == "https://cdn.dummyjson.com/product-images/12/thumbnail.jpg"
        ), f'Expected {response["products"][11]["images"][4]} to be string "https://cdn.dummyjson.com/product-images/12/thumbnail.jpg", but it is not.'
        keys_to_assert = [
            "id",
            "title",
            "description",
            "price",
            "discountPercentage",
            "rating",
            "stock",
            "brand",
            "category",
            "thumbnail",
            "images",
        ]
        for key in keys_to_assert:
            assert (
                key in response["products"][12]
            ), f"Expected {key} to be in the dictionary, but it's not."
        assert (
            response["products"][12]["id"] == 13
        ), f'Expected {response["products"][12]["id"]} to be number 13, but it is not.'
        assert (
            response["products"][12]["title"] == "Fog Scent Xpressio Perfume"
        ), f'Expected {response["products"][12]["title"]} to be string "Fog Scent Xpressio Perfume", but it is not.'
        assert (
            response["products"][12]["description"]
            == "Product details of Best Fog Scent Xpressio Perfume 100ml For Men cool long lasting perfumes for Men"
        ), f'Expected {response["products"][12]["description"]} to be string "Product details of Best Fog Scent Xpressio Perfume 100ml For Men cool long lasting perfumes for Men", but it is not.'
        assert (
            response["products"][12]["price"] == 13
        ), f'Expected {response["products"][12]["price"]} to be number 13, but it is not.'
        assert (
            response["products"][12]["discountPercentage"] == 8.14
        ), f'Expected {response["products"][12]["discountPercentage"]} to be number 8.14, but it is not.'
        assert (
            response["products"][12]["rating"] == 4.59
        ), f'Expected {response["products"][12]["rating"]} to be number 4.59, but it is not.'
        assert (
            response["products"][12]["stock"] == 61
        ), f'Expected {response["products"][12]["stock"]} to be number 61, but it is not.'
        assert (
            response["products"][12]["brand"] == "Fog Scent Xpressio"
        ), f'Expected {response["products"][12]["brand"]} to be string "Fog Scent Xpressio", but it is not.'
        assert (
            response["products"][12]["category"] == "fragrances"
        ), f'Expected {response["products"][12]["category"]} to be string "fragrances", but it is not.'
        assert (
            response["products"][12]["thumbnail"]
            == "https://cdn.dummyjson.com/product-images/13/thumbnail.webp"
        ), f'Expected {response["products"][12]["thumbnail"]} to be string "https://cdn.dummyjson.com/product-images/13/thumbnail.webp", but it is not.'
        assert isinstance(
            response["products"][12]["images"], list
        ), "Expected the object tobe a list, but it's not"
        assert (
            len(response["products"][12]["images"]) == 5
        ), "Expected the list to have length 5, but it's not"
        assert (
            response["products"][12]["images"][0]
            == "https://cdn.dummyjson.com/product-images/13/1.jpg"
        ), f'Expected {response["products"][12]["images"][0]} to be string "https://cdn.dummyjson.com/product-images/13/1.jpg", but it is not.'
        assert (
            response["products"][12]["images"][1]
            == "https://cdn.dummyjson.com/product-images/13/2.png"
        ), f'Expected {response["products"][12]["images"][1]} to be string "https://cdn.dummyjson.com/product-images/13/2.png", but it is not.'
        assert (
            response["products"][12]["images"][2]
            == "https://cdn.dummyjson.com/product-images/13/3.jpg"
        ), f'Expected {response["products"][12]["images"][2]} to be string "https://cdn.dummyjson.com/product-images/13/3.jpg", but it is not.'
        assert (
            response["products"][12]["images"][3]
            == "https://cdn.dummyjson.com/product-images/13/4.jpg"
        ), f'Expected {response["products"][12]["images"][3]} to be string "https://cdn.dummyjson.com/product-images/13/4.jpg", but it is not.'
        assert (
            response["products"][12]["images"][4]
            == "https://cdn.dummyjson.com/product-images/13/thumbnail.webp"
        ), f'Expected {response["products"][12]["images"][4]} to be string "https://cdn.dummyjson.com/product-images/13/thumbnail.webp", but it is not.'
        keys_to_assert = [
            "id",
            "title",
            "description",
            "price",
            "discountPercentage",
            "rating",
            "stock",
            "brand",
            "category",
            "thumbnail",
            "images",
        ]
        for key in keys_to_assert:
            assert (
                key in response["products"][13]
            ), f"Expected {key} to be in the dictionary, but it's not."
        assert (
            response["products"][13]["id"] == 14
        ), f'Expected {response["products"][13]["id"]} to be number 14, but it is not.'
        assert (
            response["products"][13]["title"]
            == "Non-Alcoholic Concentrated Perfume Oil"
        ), f'Expected {response["products"][13]["title"]} to be string "Non-Alcoholic Concentrated Perfume Oil", but it is not.'
        assert (
            response["products"][13]["description"]
            == "Original Al Munakh® by Mahal Al Musk | Our Impression of Climate | 6ml Non-Alcoholic Concentrated Perfume Oil"
        ), f'Expected {response["products"][13]["description"]} to be string "Original Al Munakh® by Mahal Al Musk | Our Impression of Climate | 6ml Non-Alcoholic Concentrated Perfume Oil", but it is not.'
        assert (
            response["products"][13]["price"] == 120
        ), f'Expected {response["products"][13]["price"]} to be number 120, but it is not.'
        assert (
            response["products"][13]["discountPercentage"] == 15.6
        ), f'Expected {response["products"][13]["discountPercentage"]} to be number 15.6, but it is not.'
        assert (
            response["products"][13]["rating"] == 4.21
        ), f'Expected {response["products"][13]["rating"]} to be number 4.21, but it is not.'
        assert (
            response["products"][13]["stock"] == 114
        ), f'Expected {response["products"][13]["stock"]} to be number 114, but it is not.'
        assert (
            response["products"][13]["brand"] == "Al Munakh"
        ), f'Expected {response["products"][13]["brand"]} to be string "Al Munakh", but it is not.'
        assert (
            response["products"][13]["category"] == "fragrances"
        ), f'Expected {response["products"][13]["category"]} to be string "fragrances", but it is not.'
        assert (
            response["products"][13]["thumbnail"]
            == "https://cdn.dummyjson.com/product-images/14/thumbnail.jpg"
        ), f'Expected {response["products"][13]["thumbnail"]} to be string "https://cdn.dummyjson.com/product-images/14/thumbnail.jpg", but it is not.'
        assert isinstance(
            response["products"][13]["images"], list
        ), "Expected the object tobe a list, but it's not"
        assert (
            len(response["products"][13]["images"]) == 4
        ), "Expected the list to have length 4, but it's not"
        assert (
            response["products"][13]["images"][0]
            == "https://cdn.dummyjson.com/product-images/14/1.jpg"
        ), f'Expected {response["products"][13]["images"][0]} to be string "https://cdn.dummyjson.com/product-images/14/1.jpg", but it is not.'
        assert (
            response["products"][13]["images"][1]
            == "https://cdn.dummyjson.com/product-images/14/2.jpg"
        ), f'Expected {response["products"][13]["images"][1]} to be string "https://cdn.dummyjson.com/product-images/14/2.jpg", but it is not.'
        assert (
            response["products"][13]["images"][2]
            == "https://cdn.dummyjson.com/product-images/14/3.jpg"
        ), f'Expected {response["products"][13]["images"][2]} to be string "https://cdn.dummyjson.com/product-images/14/3.jpg", but it is not.'
        assert (
            response["products"][13]["images"][3]
            == "https://cdn.dummyjson.com/product-images/14/thumbnail.jpg"
        ), f'Expected {response["products"][13]["images"][3]} to be string "https://cdn.dummyjson.com/product-images/14/thumbnail.jpg", but it is not.'
        keys_to_assert = [
            "id",
            "title",
            "description",
            "price",
            "discountPercentage",
            "rating",
            "stock",
            "brand",
            "category",
            "thumbnail",
            "images",
        ]
        for key in keys_to_assert:
            assert (
                key in response["products"][14]
            ), f"Expected {key} to be in the dictionary, but it's not."
        assert (
            response["products"][14]["id"] == 15
        ), f'Expected {response["products"][14]["id"]} to be number 15, but it is not.'
        assert (
            response["products"][14]["title"] == "Eau De Perfume Spray"
        ), f'Expected {response["products"][14]["title"]} to be string "Eau De Perfume Spray", but it is not.'
        assert (
            response["products"][14]["description"]
            == "Genuine  Al-Rehab spray perfume from UAE/Saudi Arabia/Yemen High Quality"
        ), f'Expected {response["products"][14]["description"]} to be string "Genuine  Al-Rehab spray perfume from UAE/Saudi Arabia/Yemen High Quality", but it is not.'
        assert (
            response["products"][14]["price"] == 30
        ), f'Expected {response["products"][14]["price"]} to be number 30, but it is not.'
        assert (
            response["products"][14]["discountPercentage"] == 10.99
        ), f'Expected {response["products"][14]["discountPercentage"]} to be number 10.99, but it is not.'
        assert (
            response["products"][14]["rating"] == 4.7
        ), f'Expected {response["products"][14]["rating"]} to be number 4.7, but it is not.'
        assert (
            response["products"][14]["stock"] == 105
        ), f'Expected {response["products"][14]["stock"]} to be number 105, but it is not.'
        assert (
            response["products"][14]["brand"] == "Lord - Al-Rehab"
        ), f'Expected {response["products"][14]["brand"]} to be string "Lord - Al-Rehab", but it is not.'
        assert (
            response["products"][14]["category"] == "fragrances"
        ), f'Expected {response["products"][14]["category"]} to be string "fragrances", but it is not.'
        assert (
            response["products"][14]["thumbnail"]
            == "https://cdn.dummyjson.com/product-images/15/thumbnail.jpg"
        ), f'Expected {response["products"][14]["thumbnail"]} to be string "https://cdn.dummyjson.com/product-images/15/thumbnail.jpg", but it is not.'
        assert isinstance(
            response["products"][14]["images"], list
        ), "Expected the object tobe a list, but it's not"
        assert (
            len(response["products"][14]["images"]) == 5
        ), "Expected the list to have length 5, but it's not"
        assert (
            response["products"][14]["images"][0]
            == "https://cdn.dummyjson.com/product-images/15/1.jpg"
        ), f'Expected {response["products"][14]["images"][0]} to be string "https://cdn.dummyjson.com/product-images/15/1.jpg", but it is not.'
        assert (
            response["products"][14]["images"][1]
            == "https://cdn.dummyjson.com/product-images/15/2.jpg"
        ), f'Expected {response["products"][14]["images"][1]} to be string "https://cdn.dummyjson.com/product-images/15/2.jpg", but it is not.'
        assert (
            response["products"][14]["images"][2]
            == "https://cdn.dummyjson.com/product-images/15/3.jpg"
        ), f'Expected {response["products"][14]["images"][2]} to be string "https://cdn.dummyjson.com/product-images/15/3.jpg", but it is not.'
        assert (
            response["products"][14]["images"][3]
            == "https://cdn.dummyjson.com/product-images/15/4.jpg"
        ), f'Expected {response["products"][14]["images"][3]} to be string "https://cdn.dummyjson.com/product-images/15/4.jpg", but it is not.'
        assert (
            response["products"][14]["images"][4]
            == "https://cdn.dummyjson.com/product-images/15/thumbnail.jpg"
        ), f'Expected {response["products"][14]["images"][4]} to be string "https://cdn.dummyjson.com/product-images/15/thumbnail.jpg", but it is not.'
        keys_to_assert = [
            "id",
            "title",
            "description",
            "price",
            "discountPercentage",
            "rating",
            "stock",
            "brand",
            "category",
            "thumbnail",
            "images",
        ]
        for key in keys_to_assert:
            assert (
                key in response["products"][15]
            ), f"Expected {key} to be in the dictionary, but it's not."
        assert (
            response["products"][15]["id"] == 16
        ), f'Expected {response["products"][15]["id"]} to be number 16, but it is not.'
        assert (
            response["products"][15]["title"] == "Hyaluronic Acid Serum"
        ), f'Expected {response["products"][15]["title"]} to be string "Hyaluronic Acid Serum", but it is not.'
        assert (
            response["products"][15]["description"]
            == "L'OrÃ©al Paris introduces Hyaluron Expert Replumping Serum formulated with 1.5% Hyaluronic Acid"
        ), f'Expected {response["products"][15]["description"]} to be string "L\'OrÃ©al Paris introduces Hyaluron Expert Replumping Serum formulated with 1.5% Hyaluronic Acid", but it is not.'
        assert (
            response["products"][15]["price"] == 19
        ), f'Expected {response["products"][15]["price"]} to be number 19, but it is not.'
        assert (
            response["products"][15]["discountPercentage"] == 13.31
        ), f'Expected {response["products"][15]["discountPercentage"]} to be number 13.31, but it is not.'
        assert (
            response["products"][15]["rating"] == 4.83
        ), f'Expected {response["products"][15]["rating"]} to be number 4.83, but it is not.'
        assert (
            response["products"][15]["stock"] == 110
        ), f'Expected {response["products"][15]["stock"]} to be number 110, but it is not.'
        assert (
            response["products"][15]["brand"] == "L'Oreal Paris"
        ), f'Expected {response["products"][15]["brand"]} to be string "L\'Oreal Paris", but it is not.'
        assert (
            response["products"][15]["category"] == "skincare"
        ), f'Expected {response["products"][15]["category"]} to be string "skincare", but it is not.'
        assert (
            response["products"][15]["thumbnail"]
            == "https://cdn.dummyjson.com/product-images/16/thumbnail.jpg"
        ), f'Expected {response["products"][15]["thumbnail"]} to be string "https://cdn.dummyjson.com/product-images/16/thumbnail.jpg", but it is not.'
        assert isinstance(
            response["products"][15]["images"], list
        ), "Expected the object tobe a list, but it's not"
        assert (
            len(response["products"][15]["images"]) == 5
        ), "Expected the list to have length 5, but it's not"
        assert (
            response["products"][15]["images"][0]
            == "https://cdn.dummyjson.com/product-images/16/1.png"
        ), f'Expected {response["products"][15]["images"][0]} to be string "https://cdn.dummyjson.com/product-images/16/1.png", but it is not.'
        assert (
            response["products"][15]["images"][1]
            == "https://cdn.dummyjson.com/product-images/16/2.webp"
        ), f'Expected {response["products"][15]["images"][1]} to be string "https://cdn.dummyjson.com/product-images/16/2.webp", but it is not.'
        assert (
            response["products"][15]["images"][2]
            == "https://cdn.dummyjson.com/product-images/16/3.jpg"
        ), f'Expected {response["products"][15]["images"][2]} to be string "https://cdn.dummyjson.com/product-images/16/3.jpg", but it is not.'
        assert (
            response["products"][15]["images"][3]
            == "https://cdn.dummyjson.com/product-images/16/4.jpg"
        ), f'Expected {response["products"][15]["images"][3]} to be string "https://cdn.dummyjson.com/product-images/16/4.jpg", but it is not.'
        assert (
            response["products"][15]["images"][4]
            == "https://cdn.dummyjson.com/product-images/16/thumbnail.jpg"
        ), f'Expected {response["products"][15]["images"][4]} to be string "https://cdn.dummyjson.com/product-images/16/thumbnail.jpg", but it is not.'
        keys_to_assert = [
            "id",
            "title",
            "description",
            "price",
            "discountPercentage",
            "rating",
            "stock",
            "brand",
            "category",
            "thumbnail",
            "images",
        ]
        for key in keys_to_assert:
            assert (
                key in response["products"][16]
            ), f"Expected {key} to be in the dictionary, but it's not."
        assert (
            response["products"][16]["id"] == 17
        ), f'Expected {response["products"][16]["id"]} to be number 17, but it is not.'
        assert (
            response["products"][16]["title"] == "Tree Oil 30ml"
        ), f'Expected {response["products"][16]["title"]} to be string "Tree Oil 30ml", but it is not.'
        assert (
            response["products"][16]["description"]
            == "Tea tree oil contains a number of compounds, including terpinen-4-ol, that have been shown to kill certain bacteria,"
        ), f'Expected {response["products"][16]["description"]} to be string "Tea tree oil contains a number of compounds, including terpinen-4-ol, that have been shown to kill certain bacteria,", but it is not.'
        assert (
            response["products"][16]["price"] == 12
        ), f'Expected {response["products"][16]["price"]} to be number 12, but it is not.'
        assert (
            response["products"][16]["discountPercentage"] == 4.09
        ), f'Expected {response["products"][16]["discountPercentage"]} to be number 4.09, but it is not.'
        assert (
            response["products"][16]["rating"] == 4.52
        ), f'Expected {response["products"][16]["rating"]} to be number 4.52, but it is not.'
        assert (
            response["products"][16]["stock"] == 78
        ), f'Expected {response["products"][16]["stock"]} to be number 78, but it is not.'
        assert (
            response["products"][16]["brand"] == "Hemani Tea"
        ), f'Expected {response["products"][16]["brand"]} to be string "Hemani Tea", but it is not.'
        assert (
            response["products"][16]["category"] == "skincare"
        ), f'Expected {response["products"][16]["category"]} to be string "skincare", but it is not.'
        assert (
            response["products"][16]["thumbnail"]
            == "https://cdn.dummyjson.com/product-images/17/thumbnail.jpg"
        ), f'Expected {response["products"][16]["thumbnail"]} to be string "https://cdn.dummyjson.com/product-images/17/thumbnail.jpg", but it is not.'
        assert isinstance(
            response["products"][16]["images"], list
        ), "Expected the object tobe a list, but it's not"
        assert (
            len(response["products"][16]["images"]) == 4
        ), "Expected the list to have length 4, but it's not"
        assert (
            response["products"][16]["images"][0]
            == "https://cdn.dummyjson.com/product-images/17/1.jpg"
        ), f'Expected {response["products"][16]["images"][0]} to be string "https://cdn.dummyjson.com/product-images/17/1.jpg", but it is not.'
        assert (
            response["products"][16]["images"][1]
            == "https://cdn.dummyjson.com/product-images/17/2.jpg"
        ), f'Expected {response["products"][16]["images"][1]} to be string "https://cdn.dummyjson.com/product-images/17/2.jpg", but it is not.'
        assert (
            response["products"][16]["images"][2]
            == "https://cdn.dummyjson.com/product-images/17/3.jpg"
        ), f'Expected {response["products"][16]["images"][2]} to be string "https://cdn.dummyjson.com/product-images/17/3.jpg", but it is not.'
        assert (
            response["products"][16]["images"][3]
            == "https://cdn.dummyjson.com/product-images/17/thumbnail.jpg"
        ), f'Expected {response["products"][16]["images"][3]} to be string "https://cdn.dummyjson.com/product-images/17/thumbnail.jpg", but it is not.'
        keys_to_assert = [
            "id",
            "title",
            "description",
            "price",
            "discountPercentage",
            "rating",
            "stock",
            "brand",
            "category",
            "thumbnail",
            "images",
        ]
        for key in keys_to_assert:
            assert (
                key in response["products"][17]
            ), f"Expected {key} to be in the dictionary, but it's not."
        assert (
            response["products"][17]["id"] == 18
        ), f'Expected {response["products"][17]["id"]} to be number 18, but it is not.'
        assert (
            response["products"][17]["title"] == "Oil Free Moisturizer 100ml"
        ), f'Expected {response["products"][17]["title"]} to be string "Oil Free Moisturizer 100ml", but it is not.'
        assert (
            response["products"][17]["description"]
            == "Dermive Oil Free Moisturizer with SPF 20 is specifically formulated with ceramides, hyaluronic acid & sunscreen."
        ), f'Expected {response["products"][17]["description"]} to be string "Dermive Oil Free Moisturizer with SPF 20 is specifically formulated with ceramides, hyaluronic acid & sunscreen.", but it is not.'
        assert (
            response["products"][17]["price"] == 40
        ), f'Expected {response["products"][17]["price"]} to be number 40, but it is not.'
        assert (
            response["products"][17]["discountPercentage"] == 13.1
        ), f'Expected {response["products"][17]["discountPercentage"]} to be number 13.1, but it is not.'
        assert (
            response["products"][17]["rating"] == 4.56
        ), f'Expected {response["products"][17]["rating"]} to be number 4.56, but it is not.'
        assert (
            response["products"][17]["stock"] == 88
        ), f'Expected {response["products"][17]["stock"]} to be number 88, but it is not.'
        assert (
            response["products"][17]["brand"] == "Dermive"
        ), f'Expected {response["products"][17]["brand"]} to be string "Dermive", but it is not.'
        assert (
            response["products"][17]["category"] == "skincare"
        ), f'Expected {response["products"][17]["category"]} to be string "skincare", but it is not.'
        assert (
            response["products"][17]["thumbnail"]
            == "https://cdn.dummyjson.com/product-images/18/thumbnail.jpg"
        ), f'Expected {response["products"][17]["thumbnail"]} to be string "https://cdn.dummyjson.com/product-images/18/thumbnail.jpg", but it is not.'
        assert isinstance(
            response["products"][17]["images"], list
        ), "Expected the object tobe a list, but it's not"
        assert (
            len(response["products"][17]["images"]) == 5
        ), "Expected the list to have length 5, but it's not"
        assert (
            response["products"][17]["images"][0]
            == "https://cdn.dummyjson.com/product-images/18/1.jpg"
        ), f'Expected {response["products"][17]["images"][0]} to be string "https://cdn.dummyjson.com/product-images/18/1.jpg", but it is not.'
        assert (
            response["products"][17]["images"][1]
            == "https://cdn.dummyjson.com/product-images/18/2.jpg"
        ), f'Expected {response["products"][17]["images"][1]} to be string "https://cdn.dummyjson.com/product-images/18/2.jpg", but it is not.'
        assert (
            response["products"][17]["images"][2]
            == "https://cdn.dummyjson.com/product-images/18/3.jpg"
        ), f'Expected {response["products"][17]["images"][2]} to be string "https://cdn.dummyjson.com/product-images/18/3.jpg", but it is not.'
        assert (
            response["products"][17]["images"][3]
            == "https://cdn.dummyjson.com/product-images/18/4.jpg"
        ), f'Expected {response["products"][17]["images"][3]} to be string "https://cdn.dummyjson.com/product-images/18/4.jpg", but it is not.'
        assert (
            response["products"][17]["images"][4]
            == "https://cdn.dummyjson.com/product-images/18/thumbnail.jpg"
        ), f'Expected {response["products"][17]["images"][4]} to be string "https://cdn.dummyjson.com/product-images/18/thumbnail.jpg", but it is not.'
        keys_to_assert = [
            "id",
            "title",
            "description",
            "price",
            "discountPercentage",
            "rating",
            "stock",
            "brand",
            "category",
            "thumbnail",
            "images",
        ]
        for key in keys_to_assert:
            assert (
                key in response["products"][18]
            ), f"Expected {key} to be in the dictionary, but it's not."
        assert (
            response["products"][18]["id"] == 19
        ), f'Expected {response["products"][18]["id"]} to be number 19, but it is not.'
        assert (
            response["products"][18]["title"] == "Skin Beauty Serum."
        ), f'Expected {response["products"][18]["title"]} to be string "Skin Beauty Serum.", but it is not.'
        assert (
            response["products"][18]["description"]
            == "Product name: rorec collagen hyaluronic acid white face serum riceNet weight: 15 m"
        ), f'Expected {response["products"][18]["description"]} to be string "Product name: rorec collagen hyaluronic acid white face serum riceNet weight: 15 m", but it is not.'
        assert (
            response["products"][18]["price"] == 46
        ), f'Expected {response["products"][18]["price"]} to be number 46, but it is not.'
        assert (
            response["products"][18]["discountPercentage"] == 10.68
        ), f'Expected {response["products"][18]["discountPercentage"]} to be number 10.68, but it is not.'
        assert (
            response["products"][18]["rating"] == 4.42
        ), f'Expected {response["products"][18]["rating"]} to be number 4.42, but it is not.'
        assert (
            response["products"][18]["stock"] == 54
        ), f'Expected {response["products"][18]["stock"]} to be number 54, but it is not.'
        assert (
            response["products"][18]["brand"] == "ROREC White Rice"
        ), f'Expected {response["products"][18]["brand"]} to be string "ROREC White Rice", but it is not.'
        assert (
            response["products"][18]["category"] == "skincare"
        ), f'Expected {response["products"][18]["category"]} to be string "skincare", but it is not.'
        assert (
            response["products"][18]["thumbnail"]
            == "https://cdn.dummyjson.com/product-images/19/thumbnail.jpg"
        ), f'Expected {response["products"][18]["thumbnail"]} to be string "https://cdn.dummyjson.com/product-images/19/thumbnail.jpg", but it is not.'
        assert isinstance(
            response["products"][18]["images"], list
        ), "Expected the object tobe a list, but it's not"
        assert (
            len(response["products"][18]["images"]) == 4
        ), "Expected the list to have length 4, but it's not"
        assert (
            response["products"][18]["images"][0]
            == "https://cdn.dummyjson.com/product-images/19/1.jpg"
        ), f'Expected {response["products"][18]["images"][0]} to be string "https://cdn.dummyjson.com/product-images/19/1.jpg", but it is not.'
        assert (
            response["products"][18]["images"][1]
            == "https://cdn.dummyjson.com/product-images/19/2.jpg"
        ), f'Expected {response["products"][18]["images"][1]} to be string "https://cdn.dummyjson.com/product-images/19/2.jpg", but it is not.'
        assert (
            response["products"][18]["images"][2]
            == "https://cdn.dummyjson.com/product-images/19/3.png"
        ), f'Expected {response["products"][18]["images"][2]} to be string "https://cdn.dummyjson.com/product-images/19/3.png", but it is not.'
        assert (
            response["products"][18]["images"][3]
            == "https://cdn.dummyjson.com/product-images/19/thumbnail.jpg"
        ), f'Expected {response["products"][18]["images"][3]} to be string "https://cdn.dummyjson.com/product-images/19/thumbnail.jpg", but it is not.'
        keys_to_assert = [
            "id",
            "title",
            "description",
            "price",
            "discountPercentage",
            "rating",
            "stock",
            "brand",
            "category",
            "thumbnail",
            "images",
        ]
        for key in keys_to_assert:
            assert (
                key in response["products"][19]
            ), f"Expected {key} to be in the dictionary, but it's not."
        assert (
            response["products"][19]["id"] == 20
        ), f'Expected {response["products"][19]["id"]} to be number 20, but it is not.'
        assert (
            response["products"][19]["title"] == "Freckle Treatment Cream- 15gm"
        ), f'Expected {response["products"][19]["title"]} to be string "Freckle Treatment Cream- 15gm", but it is not.'
        assert (
            response["products"][19]["description"]
            == "Fair & Clear is Pakistan's only pure Freckle cream which helpsfade Freckles, Darkspots and pigments. Mercury level is 0%, so there are no side effects."
        ), f'Expected {response["products"][19]["description"]} to be string "Fair & Clear is Pakistan\'s only pure Freckle cream which helpsfade Freckles, Darkspots and pigments. Mercury level is 0%, so there are no side effects.", but it is not.'
        assert (
            response["products"][19]["price"] == 70
        ), f'Expected {response["products"][19]["price"]} to be number 70, but it is not.'
        assert (
            response["products"][19]["discountPercentage"] == 16.99
        ), f'Expected {response["products"][19]["discountPercentage"]} to be number 16.99, but it is not.'
        assert (
            response["products"][19]["rating"] == 4.06
        ), f'Expected {response["products"][19]["rating"]} to be number 4.06, but it is not.'
        assert (
            response["products"][19]["stock"] == 140
        ), f'Expected {response["products"][19]["stock"]} to be number 140, but it is not.'
        assert (
            response["products"][19]["brand"] == "Fair & Clear"
        ), f'Expected {response["products"][19]["brand"]} to be string "Fair & Clear", but it is not.'
        assert (
            response["products"][19]["category"] == "skincare"
        ), f'Expected {response["products"][19]["category"]} to be string "skincare", but it is not.'
        assert (
            response["products"][19]["thumbnail"]
            == "https://cdn.dummyjson.com/product-images/20/thumbnail.jpg"
        ), f'Expected {response["products"][19]["thumbnail"]} to be string "https://cdn.dummyjson.com/product-images/20/thumbnail.jpg", but it is not.'
        assert isinstance(
            response["products"][19]["images"], list
        ), "Expected the object tobe a list, but it's not"
        assert (
            len(response["products"][19]["images"]) == 5
        ), "Expected the list to have length 5, but it's not"
        assert (
            response["products"][19]["images"][0]
            == "https://cdn.dummyjson.com/product-images/20/1.jpg"
        ), f'Expected {response["products"][19]["images"][0]} to be string "https://cdn.dummyjson.com/product-images/20/1.jpg", but it is not.'
        assert (
            response["products"][19]["images"][1]
            == "https://cdn.dummyjson.com/product-images/20/2.jpg"
        ), f'Expected {response["products"][19]["images"][1]} to be string "https://cdn.dummyjson.com/product-images/20/2.jpg", but it is not.'
        assert (
            response["products"][19]["images"][2]
            == "https://cdn.dummyjson.com/product-images/20/3.jpg"
        ), f'Expected {response["products"][19]["images"][2]} to be string "https://cdn.dummyjson.com/product-images/20/3.jpg", but it is not.'
        assert (
            response["products"][19]["images"][3]
            == "https://cdn.dummyjson.com/product-images/20/4.jpg"
        ), f'Expected {response["products"][19]["images"][3]} to be string "https://cdn.dummyjson.com/product-images/20/4.jpg", but it is not.'
        assert (
            response["products"][19]["images"][4]
            == "https://cdn.dummyjson.com/product-images/20/thumbnail.jpg"
        ), f'Expected {response["products"][19]["images"][4]} to be string "https://cdn.dummyjson.com/product-images/20/thumbnail.jpg", but it is not.'
        keys_to_assert = [
            "id",
            "title",
            "description",
            "price",
            "discountPercentage",
            "rating",
            "stock",
            "brand",
            "category",
            "thumbnail",
            "images",
        ]
        for key in keys_to_assert:
            assert (
                key in response["products"][20]
            ), f"Expected {key} to be in the dictionary, but it's not."
        assert (
            response["products"][20]["id"] == 21
        ), f'Expected {response["products"][20]["id"]} to be number 21, but it is not.'
        assert (
            response["products"][20]["title"] == "- Daal Masoor 500 grams"
        ), f'Expected {response["products"][20]["title"]} to be string "- Daal Masoor 500 grams", but it is not.'
        assert (
            response["products"][20]["description"]
            == "Fine quality Branded Product Keep in a cool and dry place"
        ), f'Expected {response["products"][20]["description"]} to be string "Fine quality Branded Product Keep in a cool and dry place", but it is not.'
        assert (
            response["products"][20]["price"] == 20
        ), f'Expected {response["products"][20]["price"]} to be number 20, but it is not.'
        assert (
            response["products"][20]["discountPercentage"] == 4.81
        ), f'Expected {response["products"][20]["discountPercentage"]} to be number 4.81, but it is not.'
        assert (
            response["products"][20]["rating"] == 4.44
        ), f'Expected {response["products"][20]["rating"]} to be number 4.44, but it is not.'
        assert (
            response["products"][20]["stock"] == 133
        ), f'Expected {response["products"][20]["stock"]} to be number 133, but it is not.'
        assert (
            response["products"][20]["brand"] == "Saaf & Khaas"
        ), f'Expected {response["products"][20]["brand"]} to be string "Saaf & Khaas", but it is not.'
        assert (
            response["products"][20]["category"] == "groceries"
        ), f'Expected {response["products"][20]["category"]} to be string "groceries", but it is not.'
        assert (
            response["products"][20]["thumbnail"]
            == "https://cdn.dummyjson.com/product-images/21/thumbnail.png"
        ), f'Expected {response["products"][20]["thumbnail"]} to be string "https://cdn.dummyjson.com/product-images/21/thumbnail.png", but it is not.'
        assert isinstance(
            response["products"][20]["images"], list
        ), "Expected the object tobe a list, but it's not"
        assert (
            len(response["products"][20]["images"]) == 3
        ), "Expected the list to have length 3, but it's not"
        assert (
            response["products"][20]["images"][0]
            == "https://cdn.dummyjson.com/product-images/21/1.png"
        ), f'Expected {response["products"][20]["images"][0]} to be string "https://cdn.dummyjson.com/product-images/21/1.png", but it is not.'
        assert (
            response["products"][20]["images"][1]
            == "https://cdn.dummyjson.com/product-images/21/2.jpg"
        ), f'Expected {response["products"][20]["images"][1]} to be string "https://cdn.dummyjson.com/product-images/21/2.jpg", but it is not.'
        assert (
            response["products"][20]["images"][2]
            == "https://cdn.dummyjson.com/product-images/21/3.jpg"
        ), f'Expected {response["products"][20]["images"][2]} to be string "https://cdn.dummyjson.com/product-images/21/3.jpg", but it is not.'
        keys_to_assert = [
            "id",
            "title",
            "description",
            "price",
            "discountPercentage",
            "rating",
            "stock",
            "brand",
            "category",
            "thumbnail",
            "images",
        ]
        for key in keys_to_assert:
            assert (
                key in response["products"][21]
            ), f"Expected {key} to be in the dictionary, but it's not."
        assert (
            response["products"][21]["id"] == 22
        ), f'Expected {response["products"][21]["id"]} to be number 22, but it is not.'
        assert (
            response["products"][21]["title"] == "Elbow Macaroni - 400 gm"
        ), f'Expected {response["products"][21]["title"]} to be string "Elbow Macaroni - 400 gm", but it is not.'
        assert (
            response["products"][21]["description"]
            == "Product details of Bake Parlor Big Elbow Macaroni - 400 gm"
        ), f'Expected {response["products"][21]["description"]} to be string "Product details of Bake Parlor Big Elbow Macaroni - 400 gm", but it is not.'
        assert (
            response["products"][21]["price"] == 14
        ), f'Expected {response["products"][21]["price"]} to be number 14, but it is not.'
        assert (
            response["products"][21]["discountPercentage"] == 15.58
        ), f'Expected {response["products"][21]["discountPercentage"]} to be number 15.58, but it is not.'
        assert (
            response["products"][21]["rating"] == 4.57
        ), f'Expected {response["products"][21]["rating"]} to be number 4.57, but it is not.'
        assert (
            response["products"][21]["stock"] == 146
        ), f'Expected {response["products"][21]["stock"]} to be number 146, but it is not.'
        assert (
            response["products"][21]["brand"] == "Bake Parlor Big"
        ), f'Expected {response["products"][21]["brand"]} to be string "Bake Parlor Big", but it is not.'
        assert (
            response["products"][21]["category"] == "groceries"
        ), f'Expected {response["products"][21]["category"]} to be string "groceries", but it is not.'
        assert (
            response["products"][21]["thumbnail"]
            == "https://cdn.dummyjson.com/product-images/22/thumbnail.jpg"
        ), f'Expected {response["products"][21]["thumbnail"]} to be string "https://cdn.dummyjson.com/product-images/22/thumbnail.jpg", but it is not.'
        assert isinstance(
            response["products"][21]["images"], list
        ), "Expected the object tobe a list, but it's not"
        assert (
            len(response["products"][21]["images"]) == 3
        ), "Expected the list to have length 3, but it's not"
        assert (
            response["products"][21]["images"][0]
            == "https://cdn.dummyjson.com/product-images/22/1.jpg"
        ), f'Expected {response["products"][21]["images"][0]} to be string "https://cdn.dummyjson.com/product-images/22/1.jpg", but it is not.'
        assert (
            response["products"][21]["images"][1]
            == "https://cdn.dummyjson.com/product-images/22/2.jpg"
        ), f'Expected {response["products"][21]["images"][1]} to be string "https://cdn.dummyjson.com/product-images/22/2.jpg", but it is not.'
        assert (
            response["products"][21]["images"][2]
            == "https://cdn.dummyjson.com/product-images/22/3.jpg"
        ), f'Expected {response["products"][21]["images"][2]} to be string "https://cdn.dummyjson.com/product-images/22/3.jpg", but it is not.'
        keys_to_assert = [
            "id",
            "title",
            "description",
            "price",
            "discountPercentage",
            "rating",
            "stock",
            "brand",
            "category",
            "thumbnail",
            "images",
        ]
        for key in keys_to_assert:
            assert (
                key in response["products"][22]
            ), f"Expected {key} to be in the dictionary, but it's not."
        assert (
            response["products"][22]["id"] == 23
        ), f'Expected {response["products"][22]["id"]} to be number 23, but it is not.'
        assert (
            response["products"][22]["title"] == "Orange Essence Food Flavou"
        ), f'Expected {response["products"][22]["title"]} to be string "Orange Essence Food Flavou", but it is not.'
        assert (
            response["products"][22]["description"]
            == "Specifications of Orange Essence Food Flavour For Cakes and Baking Food Item"
        ), f'Expected {response["products"][22]["description"]} to be string "Specifications of Orange Essence Food Flavour For Cakes and Baking Food Item", but it is not.'
        assert (
            response["products"][22]["price"] == 14
        ), f'Expected {response["products"][22]["price"]} to be number 14, but it is not.'
        assert (
            response["products"][22]["discountPercentage"] == 8.04
        ), f'Expected {response["products"][22]["discountPercentage"]} to be number 8.04, but it is not.'
        assert (
            response["products"][22]["rating"] == 4.85
        ), f'Expected {response["products"][22]["rating"]} to be number 4.85, but it is not.'
        assert (
            response["products"][22]["stock"] == 26
        ), f'Expected {response["products"][22]["stock"]} to be number 26, but it is not.'
        assert (
            response["products"][22]["brand"] == "Baking Food Items"
        ), f'Expected {response["products"][22]["brand"]} to be string "Baking Food Items", but it is not.'
        assert (
            response["products"][22]["category"] == "groceries"
        ), f'Expected {response["products"][22]["category"]} to be string "groceries", but it is not.'
        assert (
            response["products"][22]["thumbnail"]
            == "https://cdn.dummyjson.com/product-images/23/thumbnail.jpg"
        ), f'Expected {response["products"][22]["thumbnail"]} to be string "https://cdn.dummyjson.com/product-images/23/thumbnail.jpg", but it is not.'
        assert isinstance(
            response["products"][22]["images"], list
        ), "Expected the object tobe a list, but it's not"
        assert (
            len(response["products"][22]["images"]) == 5
        ), "Expected the list to have length 5, but it's not"
        assert (
            response["products"][22]["images"][0]
            == "https://cdn.dummyjson.com/product-images/23/1.jpg"
        ), f'Expected {response["products"][22]["images"][0]} to be string "https://cdn.dummyjson.com/product-images/23/1.jpg", but it is not.'
        assert (
            response["products"][22]["images"][1]
            == "https://cdn.dummyjson.com/product-images/23/2.jpg"
        ), f'Expected {response["products"][22]["images"][1]} to be string "https://cdn.dummyjson.com/product-images/23/2.jpg", but it is not.'
        assert (
            response["products"][22]["images"][2]
            == "https://cdn.dummyjson.com/product-images/23/3.jpg"
        ), f'Expected {response["products"][22]["images"][2]} to be string "https://cdn.dummyjson.com/product-images/23/3.jpg", but it is not.'
        assert (
            response["products"][22]["images"][3]
            == "https://cdn.dummyjson.com/product-images/23/4.jpg"
        ), f'Expected {response["products"][22]["images"][3]} to be string "https://cdn.dummyjson.com/product-images/23/4.jpg", but it is not.'
        assert (
            response["products"][22]["images"][4]
            == "https://cdn.dummyjson.com/product-images/23/thumbnail.jpg"
        ), f'Expected {response["products"][22]["images"][4]} to be string "https://cdn.dummyjson.com/product-images/23/thumbnail.jpg", but it is not.'
        keys_to_assert = [
            "id",
            "title",
            "description",
            "price",
            "discountPercentage",
            "rating",
            "stock",
            "brand",
            "category",
            "thumbnail",
            "images",
        ]
        for key in keys_to_assert:
            assert (
                key in response["products"][23]
            ), f"Expected {key} to be in the dictionary, but it's not."
        assert (
            response["products"][23]["id"] == 24
        ), f'Expected {response["products"][23]["id"]} to be number 24, but it is not.'
        assert (
            response["products"][23]["title"] == "cereals muesli fruit nuts"
        ), f'Expected {response["products"][23]["title"]} to be string "cereals muesli fruit nuts", but it is not.'
        assert (
            response["products"][23]["description"]
            == "original fauji cereal muesli 250gm box pack original fauji cereals muesli fruit nuts flakes breakfast cereal break fast faujicereals cerels cerel foji fouji"
        ), f'Expected {response["products"][23]["description"]} to be string "original fauji cereal muesli 250gm box pack original fauji cereals muesli fruit nuts flakes breakfast cereal break fast faujicereals cerels cerel foji fouji", but it is not.'
        assert (
            response["products"][23]["price"] == 46
        ), f'Expected {response["products"][23]["price"]} to be number 46, but it is not.'
        assert (
            response["products"][23]["discountPercentage"] == 16.8
        ), f'Expected {response["products"][23]["discountPercentage"]} to be number 16.8, but it is not.'
        assert (
            response["products"][23]["rating"] == 4.94
        ), f'Expected {response["products"][23]["rating"]} to be number 4.94, but it is not.'
        assert (
            response["products"][23]["stock"] == 113
        ), f'Expected {response["products"][23]["stock"]} to be number 113, but it is not.'
        assert (
            response["products"][23]["brand"] == "fauji"
        ), f'Expected {response["products"][23]["brand"]} to be string "fauji", but it is not.'
        assert (
            response["products"][23]["category"] == "groceries"
        ), f'Expected {response["products"][23]["category"]} to be string "groceries", but it is not.'
        assert (
            response["products"][23]["thumbnail"]
            == "https://cdn.dummyjson.com/product-images/24/thumbnail.jpg"
        ), f'Expected {response["products"][23]["thumbnail"]} to be string "https://cdn.dummyjson.com/product-images/24/thumbnail.jpg", but it is not.'
        assert isinstance(
            response["products"][23]["images"], list
        ), "Expected the object tobe a list, but it's not"
        assert (
            len(response["products"][23]["images"]) == 5
        ), "Expected the list to have length 5, but it's not"
        assert (
            response["products"][23]["images"][0]
            == "https://cdn.dummyjson.com/product-images/24/1.jpg"
        ), f'Expected {response["products"][23]["images"][0]} to be string "https://cdn.dummyjson.com/product-images/24/1.jpg", but it is not.'
        assert (
            response["products"][23]["images"][1]
            == "https://cdn.dummyjson.com/product-images/24/2.jpg"
        ), f'Expected {response["products"][23]["images"][1]} to be string "https://cdn.dummyjson.com/product-images/24/2.jpg", but it is not.'
        assert (
            response["products"][23]["images"][2]
            == "https://cdn.dummyjson.com/product-images/24/3.jpg"
        ), f'Expected {response["products"][23]["images"][2]} to be string "https://cdn.dummyjson.com/product-images/24/3.jpg", but it is not.'
        assert (
            response["products"][23]["images"][3]
            == "https://cdn.dummyjson.com/product-images/24/4.jpg"
        ), f'Expected {response["products"][23]["images"][3]} to be string "https://cdn.dummyjson.com/product-images/24/4.jpg", but it is not.'
        assert (
            response["products"][23]["images"][4]
            == "https://cdn.dummyjson.com/product-images/24/thumbnail.jpg"
        ), f'Expected {response["products"][23]["images"][4]} to be string "https://cdn.dummyjson.com/product-images/24/thumbnail.jpg", but it is not.'
        keys_to_assert = [
            "id",
            "title",
            "description",
            "price",
            "discountPercentage",
            "rating",
            "stock",
            "brand",
            "category",
            "thumbnail",
            "images",
        ]
        for key in keys_to_assert:
            assert (
                key in response["products"][24]
            ), f"Expected {key} to be in the dictionary, but it's not."
        assert (
            response["products"][24]["id"] == 25
        ), f'Expected {response["products"][24]["id"]} to be number 25, but it is not.'
        assert (
            response["products"][24]["title"] == "Gulab Powder 50 Gram"
        ), f'Expected {response["products"][24]["title"]} to be string "Gulab Powder 50 Gram", but it is not.'
        assert (
            response["products"][24]["description"]
            == "Dry Rose Flower Powder Gulab Powder 50 Gram • Treats Wounds"
        ), f'Expected {response["products"][24]["description"]} to be string "Dry Rose Flower Powder Gulab Powder 50 Gram • Treats Wounds", but it is not.'
        assert (
            response["products"][24]["price"] == 70
        ), f'Expected {response["products"][24]["price"]} to be number 70, but it is not.'
        assert (
            response["products"][24]["discountPercentage"] == 13.58
        ), f'Expected {response["products"][24]["discountPercentage"]} to be number 13.58, but it is not.'
        assert (
            response["products"][24]["rating"] == 4.87
        ), f'Expected {response["products"][24]["rating"]} to be number 4.87, but it is not.'
        assert (
            response["products"][24]["stock"] == 47
        ), f'Expected {response["products"][24]["stock"]} to be number 47, but it is not.'
        assert (
            response["products"][24]["brand"] == "Dry Rose"
        ), f'Expected {response["products"][24]["brand"]} to be string "Dry Rose", but it is not.'
        assert (
            response["products"][24]["category"] == "groceries"
        ), f'Expected {response["products"][24]["category"]} to be string "groceries", but it is not.'
        assert (
            response["products"][24]["thumbnail"]
            == "https://cdn.dummyjson.com/product-images/25/thumbnail.jpg"
        ), f'Expected {response["products"][24]["thumbnail"]} to be string "https://cdn.dummyjson.com/product-images/25/thumbnail.jpg", but it is not.'
        assert isinstance(
            response["products"][24]["images"], list
        ), "Expected the object tobe a list, but it's not"
        assert (
            len(response["products"][24]["images"]) == 5
        ), "Expected the list to have length 5, but it's not"
        assert (
            response["products"][24]["images"][0]
            == "https://cdn.dummyjson.com/product-images/25/1.png"
        ), f'Expected {response["products"][24]["images"][0]} to be string "https://cdn.dummyjson.com/product-images/25/1.png", but it is not.'
        assert (
            response["products"][24]["images"][1]
            == "https://cdn.dummyjson.com/product-images/25/2.jpg"
        ), f'Expected {response["products"][24]["images"][1]} to be string "https://cdn.dummyjson.com/product-images/25/2.jpg", but it is not.'
        assert (
            response["products"][24]["images"][2]
            == "https://cdn.dummyjson.com/product-images/25/3.png"
        ), f'Expected {response["products"][24]["images"][2]} to be string "https://cdn.dummyjson.com/product-images/25/3.png", but it is not.'
        assert (
            response["products"][24]["images"][3]
            == "https://cdn.dummyjson.com/product-images/25/4.jpg"
        ), f'Expected {response["products"][24]["images"][3]} to be string "https://cdn.dummyjson.com/product-images/25/4.jpg", but it is not.'
        assert (
            response["products"][24]["images"][4]
            == "https://cdn.dummyjson.com/product-images/25/thumbnail.jpg"
        ), f'Expected {response["products"][24]["images"][4]} to be string "https://cdn.dummyjson.com/product-images/25/thumbnail.jpg", but it is not.'
        keys_to_assert = [
            "id",
            "title",
            "description",
            "price",
            "discountPercentage",
            "rating",
            "stock",
            "brand",
            "category",
            "thumbnail",
            "images",
        ]
        for key in keys_to_assert:
            assert (
                key in response["products"][25]
            ), f"Expected {key} to be in the dictionary, but it's not."
        assert (
            response["products"][25]["id"] == 26
        ), f'Expected {response["products"][25]["id"]} to be number 26, but it is not.'
        assert (
            response["products"][25]["title"] == "Plant Hanger For Home"
        ), f'Expected {response["products"][25]["title"]} to be string "Plant Hanger For Home", but it is not.'
        assert (
            response["products"][25]["description"]
            == "Boho Decor Plant Hanger For Home Wall Decoration Macrame Wall Hanging Shelf"
        ), f'Expected {response["products"][25]["description"]} to be string "Boho Decor Plant Hanger For Home Wall Decoration Macrame Wall Hanging Shelf", but it is not.'
        assert (
            response["products"][25]["price"] == 41
        ), f'Expected {response["products"][25]["price"]} to be number 41, but it is not.'
        assert (
            response["products"][25]["discountPercentage"] == 17.86
        ), f'Expected {response["products"][25]["discountPercentage"]} to be number 17.86, but it is not.'
        assert (
            response["products"][25]["rating"] == 4.08
        ), f'Expected {response["products"][25]["rating"]} to be number 4.08, but it is not.'
        assert (
            response["products"][25]["stock"] == 131
        ), f'Expected {response["products"][25]["stock"]} to be number 131, but it is not.'
        assert (
            response["products"][25]["brand"] == "Boho Decor"
        ), f'Expected {response["products"][25]["brand"]} to be string "Boho Decor", but it is not.'
        assert (
            response["products"][25]["category"] == "home-decoration"
        ), f'Expected {response["products"][25]["category"]} to be string "home-decoration", but it is not.'
        assert (
            response["products"][25]["thumbnail"]
            == "https://cdn.dummyjson.com/product-images/26/thumbnail.jpg"
        ), f'Expected {response["products"][25]["thumbnail"]} to be string "https://cdn.dummyjson.com/product-images/26/thumbnail.jpg", but it is not.'
        assert isinstance(
            response["products"][25]["images"], list
        ), "Expected the object tobe a list, but it's not"
        assert (
            len(response["products"][25]["images"]) == 6
        ), "Expected the list to have length 6, but it's not"
        assert (
            response["products"][25]["images"][0]
            == "https://cdn.dummyjson.com/product-images/26/1.jpg"
        ), f'Expected {response["products"][25]["images"][0]} to be string "https://cdn.dummyjson.com/product-images/26/1.jpg", but it is not.'
        assert (
            response["products"][25]["images"][1]
            == "https://cdn.dummyjson.com/product-images/26/2.jpg"
        ), f'Expected {response["products"][25]["images"][1]} to be string "https://cdn.dummyjson.com/product-images/26/2.jpg", but it is not.'
        assert (
            response["products"][25]["images"][2]
            == "https://cdn.dummyjson.com/product-images/26/3.jpg"
        ), f'Expected {response["products"][25]["images"][2]} to be string "https://cdn.dummyjson.com/product-images/26/3.jpg", but it is not.'
        assert (
            response["products"][25]["images"][3]
            == "https://cdn.dummyjson.com/product-images/26/4.jpg"
        ), f'Expected {response["products"][25]["images"][3]} to be string "https://cdn.dummyjson.com/product-images/26/4.jpg", but it is not.'
        assert (
            response["products"][25]["images"][4]
            == "https://cdn.dummyjson.com/product-images/26/5.jpg"
        ), f'Expected {response["products"][25]["images"][4]} to be string "https://cdn.dummyjson.com/product-images/26/5.jpg", but it is not.'
        assert (
            response["products"][25]["images"][5]
            == "https://cdn.dummyjson.com/product-images/26/thumbnail.jpg"
        ), f'Expected {response["products"][25]["images"][5]} to be string "https://cdn.dummyjson.com/product-images/26/thumbnail.jpg", but it is not.'
        keys_to_assert = [
            "id",
            "title",
            "description",
            "price",
            "discountPercentage",
            "rating",
            "stock",
            "brand",
            "category",
            "thumbnail",
            "images",
        ]
        for key in keys_to_assert:
            assert (
                key in response["products"][26]
            ), f"Expected {key} to be in the dictionary, but it's not."
        assert (
            response["products"][26]["id"] == 27
        ), f'Expected {response["products"][26]["id"]} to be number 27, but it is not.'
        assert (
            response["products"][26]["title"] == "Flying Wooden Bird"
        ), f'Expected {response["products"][26]["title"]} to be string "Flying Wooden Bird", but it is not.'
        assert (
            response["products"][26]["description"]
            == "Package Include 6 Birds with Adhesive Tape Shape: 3D Shaped Wooden Birds Material: Wooden MDF, Laminated 3.5mm"
        ), f'Expected {response["products"][26]["description"]} to be string "Package Include 6 Birds with Adhesive Tape Shape: 3D Shaped Wooden Birds Material: Wooden MDF, Laminated 3.5mm", but it is not.'
        assert (
            response["products"][26]["price"] == 51
        ), f'Expected {response["products"][26]["price"]} to be number 51, but it is not.'
        assert (
            response["products"][26]["discountPercentage"] == 15.58
        ), f'Expected {response["products"][26]["discountPercentage"]} to be number 15.58, but it is not.'
        assert (
            response["products"][26]["rating"] == 4.41
        ), f'Expected {response["products"][26]["rating"]} to be number 4.41, but it is not.'
        assert (
            response["products"][26]["stock"] == 17
        ), f'Expected {response["products"][26]["stock"]} to be number 17, but it is not.'
        assert (
            response["products"][26]["brand"] == "Flying Wooden"
        ), f'Expected {response["products"][26]["brand"]} to be string "Flying Wooden", but it is not.'
        assert (
            response["products"][26]["category"] == "home-decoration"
        ), f'Expected {response["products"][26]["category"]} to be string "home-decoration", but it is not.'
        assert (
            response["products"][26]["thumbnail"]
            == "https://cdn.dummyjson.com/product-images/27/thumbnail.webp"
        ), f'Expected {response["products"][26]["thumbnail"]} to be string "https://cdn.dummyjson.com/product-images/27/thumbnail.webp", but it is not.'
        assert isinstance(
            response["products"][26]["images"], list
        ), "Expected the object tobe a list, but it's not"
        assert (
            len(response["products"][26]["images"]) == 5
        ), "Expected the list to have length 5, but it's not"
        assert (
            response["products"][26]["images"][0]
            == "https://cdn.dummyjson.com/product-images/27/1.jpg"
        ), f'Expected {response["products"][26]["images"][0]} to be string "https://cdn.dummyjson.com/product-images/27/1.jpg", but it is not.'
        assert (
            response["products"][26]["images"][1]
            == "https://cdn.dummyjson.com/product-images/27/2.jpg"
        ), f'Expected {response["products"][26]["images"][1]} to be string "https://cdn.dummyjson.com/product-images/27/2.jpg", but it is not.'
        assert (
            response["products"][26]["images"][2]
            == "https://cdn.dummyjson.com/product-images/27/3.jpg"
        ), f'Expected {response["products"][26]["images"][2]} to be string "https://cdn.dummyjson.com/product-images/27/3.jpg", but it is not.'
        assert (
            response["products"][26]["images"][3]
            == "https://cdn.dummyjson.com/product-images/27/4.jpg"
        ), f'Expected {response["products"][26]["images"][3]} to be string "https://cdn.dummyjson.com/product-images/27/4.jpg", but it is not.'
        assert (
            response["products"][26]["images"][4]
            == "https://cdn.dummyjson.com/product-images/27/thumbnail.webp"
        ), f'Expected {response["products"][26]["images"][4]} to be string "https://cdn.dummyjson.com/product-images/27/thumbnail.webp", but it is not.'
        keys_to_assert = [
            "id",
            "title",
            "description",
            "price",
            "discountPercentage",
            "rating",
            "stock",
            "brand",
            "category",
            "thumbnail",
            "images",
        ]
        for key in keys_to_assert:
            assert (
                key in response["products"][27]
            ), f"Expected {key} to be in the dictionary, but it's not."
        assert (
            response["products"][27]["id"] == 28
        ), f'Expected {response["products"][27]["id"]} to be number 28, but it is not.'
        assert (
            response["products"][27]["title"] == "3D Embellishment Art Lamp"
        ), f'Expected {response["products"][27]["title"]} to be string "3D Embellishment Art Lamp", but it is not.'
        assert (
            response["products"][27]["description"]
            == "3D led lamp sticker Wall sticker 3d wall art light on/off button  cell operated (included)"
        ), f'Expected {response["products"][27]["description"]} to be string "3D led lamp sticker Wall sticker 3d wall art light on/off button  cell operated (included)", but it is not.'
        assert (
            response["products"][27]["price"] == 20
        ), f'Expected {response["products"][27]["price"]} to be number 20, but it is not.'
        assert (
            response["products"][27]["discountPercentage"] == 16.49
        ), f'Expected {response["products"][27]["discountPercentage"]} to be number 16.49, but it is not.'
        assert (
            response["products"][27]["rating"] == 4.82
        ), f'Expected {response["products"][27]["rating"]} to be number 4.82, but it is not.'
        assert (
            response["products"][27]["stock"] == 54
        ), f'Expected {response["products"][27]["stock"]} to be number 54, but it is not.'
        assert (
            response["products"][27]["brand"] == "LED Lights"
        ), f'Expected {response["products"][27]["brand"]} to be string "LED Lights", but it is not.'
        assert (
            response["products"][27]["category"] == "home-decoration"
        ), f'Expected {response["products"][27]["category"]} to be string "home-decoration", but it is not.'
        assert (
            response["products"][27]["thumbnail"]
            == "https://cdn.dummyjson.com/product-images/28/thumbnail.jpg"
        ), f'Expected {response["products"][27]["thumbnail"]} to be string "https://cdn.dummyjson.com/product-images/28/thumbnail.jpg", but it is not.'
        assert isinstance(
            response["products"][27]["images"], list
        ), "Expected the object tobe a list, but it's not"
        assert (
            len(response["products"][27]["images"]) == 5
        ), "Expected the list to have length 5, but it's not"
        assert (
            response["products"][27]["images"][0]
            == "https://cdn.dummyjson.com/product-images/28/1.jpg"
        ), f'Expected {response["products"][27]["images"][0]} to be string "https://cdn.dummyjson.com/product-images/28/1.jpg", but it is not.'
        assert (
            response["products"][27]["images"][1]
            == "https://cdn.dummyjson.com/product-images/28/2.jpg"
        ), f'Expected {response["products"][27]["images"][1]} to be string "https://cdn.dummyjson.com/product-images/28/2.jpg", but it is not.'
        assert (
            response["products"][27]["images"][2]
            == "https://cdn.dummyjson.com/product-images/28/3.png"
        ), f'Expected {response["products"][27]["images"][2]} to be string "https://cdn.dummyjson.com/product-images/28/3.png", but it is not.'
        assert (
            response["products"][27]["images"][3]
            == "https://cdn.dummyjson.com/product-images/28/4.jpg"
        ), f'Expected {response["products"][27]["images"][3]} to be string "https://cdn.dummyjson.com/product-images/28/4.jpg", but it is not.'
        assert (
            response["products"][27]["images"][4]
            == "https://cdn.dummyjson.com/product-images/28/thumbnail.jpg"
        ), f'Expected {response["products"][27]["images"][4]} to be string "https://cdn.dummyjson.com/product-images/28/thumbnail.jpg", but it is not.'
        keys_to_assert = [
            "id",
            "title",
            "description",
            "price",
            "discountPercentage",
            "rating",
            "stock",
            "brand",
            "category",
            "thumbnail",
            "images",
        ]
        for key in keys_to_assert:
            assert (
                key in response["products"][28]
            ), f"Expected {key} to be in the dictionary, but it's not."
        assert (
            response["products"][28]["id"] == 29
        ), f'Expected {response["products"][28]["id"]} to be number 29, but it is not.'
        assert (
            response["products"][28]["title"] == "Handcraft Chinese style"
        ), f'Expected {response["products"][28]["title"]} to be string "Handcraft Chinese style", but it is not.'
        assert (
            response["products"][28]["description"]
            == "Handcraft Chinese style art luxury palace hotel villa mansion home decor ceramic vase with brass fruit plate"
        ), f'Expected {response["products"][28]["description"]} to be string "Handcraft Chinese style art luxury palace hotel villa mansion home decor ceramic vase with brass fruit plate", but it is not.'
        assert (
            response["products"][28]["price"] == 60
        ), f'Expected {response["products"][28]["price"]} to be number 60, but it is not.'
        assert (
            response["products"][28]["discountPercentage"] == 15.34
        ), f'Expected {response["products"][28]["discountPercentage"]} to be number 15.34, but it is not.'
        assert (
            response["products"][28]["rating"] == 4.44
        ), f'Expected {response["products"][28]["rating"]} to be number 4.44, but it is not.'
        assert (
            response["products"][28]["stock"] == 7
        ), f'Expected {response["products"][28]["stock"]} to be number 7, but it is not.'
        assert (
            response["products"][28]["brand"] == "luxury palace"
        ), f'Expected {response["products"][28]["brand"]} to be string "luxury palace", but it is not.'
        assert (
            response["products"][28]["category"] == "home-decoration"
        ), f'Expected {response["products"][28]["category"]} to be string "home-decoration", but it is not.'
        assert (
            response["products"][28]["thumbnail"]
            == "https://cdn.dummyjson.com/product-images/29/thumbnail.webp"
        ), f'Expected {response["products"][28]["thumbnail"]} to be string "https://cdn.dummyjson.com/product-images/29/thumbnail.webp", but it is not.'
        assert isinstance(
            response["products"][28]["images"], list
        ), "Expected the object tobe a list, but it's not"
        assert (
            len(response["products"][28]["images"]) == 5
        ), "Expected the list to have length 5, but it's not"
        assert (
            response["products"][28]["images"][0]
            == "https://cdn.dummyjson.com/product-images/29/1.jpg"
        ), f'Expected {response["products"][28]["images"][0]} to be string "https://cdn.dummyjson.com/product-images/29/1.jpg", but it is not.'
        assert (
            response["products"][28]["images"][1]
            == "https://cdn.dummyjson.com/product-images/29/2.jpg"
        ), f'Expected {response["products"][28]["images"][1]} to be string "https://cdn.dummyjson.com/product-images/29/2.jpg", but it is not.'
        assert (
            response["products"][28]["images"][2]
            == "https://cdn.dummyjson.com/product-images/29/3.webp"
        ), f'Expected {response["products"][28]["images"][2]} to be string "https://cdn.dummyjson.com/product-images/29/3.webp", but it is not.'
        assert (
            response["products"][28]["images"][3]
            == "https://cdn.dummyjson.com/product-images/29/4.webp"
        ), f'Expected {response["products"][28]["images"][3]} to be string "https://cdn.dummyjson.com/product-images/29/4.webp", but it is not.'
        assert (
            response["products"][28]["images"][4]
            == "https://cdn.dummyjson.com/product-images/29/thumbnail.webp"
        ), f'Expected {response["products"][28]["images"][4]} to be string "https://cdn.dummyjson.com/product-images/29/thumbnail.webp", but it is not.'
        keys_to_assert = [
            "id",
            "title",
            "description",
            "price",
            "discountPercentage",
            "rating",
            "stock",
            "brand",
            "category",
            "thumbnail",
            "images",
        ]
        for key in keys_to_assert:
            assert (
                key in response["products"][29]
            ), f"Expected {key} to be in the dictionary, but it's not."
        assert (
            response["products"][29]["id"] == 30
        ), f'Expected {response["products"][29]["id"]} to be number 30, but it is not.'
        assert (
            response["products"][29]["title"] == "Key Holder"
        ), f'Expected {response["products"][29]["title"]} to be string "Key Holder", but it is not.'
        assert (
            response["products"][29]["description"]
            == "Attractive DesignMetallic materialFour key hooksReliable & DurablePremium Quality"
        ), f'Expected {response["products"][29]["description"]} to be string "Attractive DesignMetallic materialFour key hooksReliable & DurablePremium Quality", but it is not.'
        assert (
            response["products"][29]["price"] == 30
        ), f'Expected {response["products"][29]["price"]} to be number 30, but it is not.'
        assert (
            response["products"][29]["discountPercentage"] == 2.92
        ), f'Expected {response["products"][29]["discountPercentage"]} to be number 2.92, but it is not.'
        assert (
            response["products"][29]["rating"] == 4.92
        ), f'Expected {response["products"][29]["rating"]} to be number 4.92, but it is not.'
        assert (
            response["products"][29]["stock"] == 54
        ), f'Expected {response["products"][29]["stock"]} to be number 54, but it is not.'
        assert (
            response["products"][29]["brand"] == "Golden"
        ), f'Expected {response["products"][29]["brand"]} to be string "Golden", but it is not.'
        assert (
            response["products"][29]["category"] == "home-decoration"
        ), f'Expected {response["products"][29]["category"]} to be string "home-decoration", but it is not.'
        assert (
            response["products"][29]["thumbnail"]
            == "https://cdn.dummyjson.com/product-images/30/thumbnail.jpg"
        ), f'Expected {response["products"][29]["thumbnail"]} to be string "https://cdn.dummyjson.com/product-images/30/thumbnail.jpg", but it is not.'
        assert isinstance(
            response["products"][29]["images"], list
        ), "Expected the object tobe a list, but it's not"
        assert (
            len(response["products"][29]["images"]) == 4
        ), "Expected the list to have length 4, but it's not"
        assert (
            response["products"][29]["images"][0]
            == "https://cdn.dummyjson.com/product-images/30/1.jpg"
        ), f'Expected {response["products"][29]["images"][0]} to be string "https://cdn.dummyjson.com/product-images/30/1.jpg", but it is not.'
        assert (
            response["products"][29]["images"][1]
            == "https://cdn.dummyjson.com/product-images/30/2.jpg"
        ), f'Expected {response["products"][29]["images"][1]} to be string "https://cdn.dummyjson.com/product-images/30/2.jpg", but it is not.'
        assert (
            response["products"][29]["images"][2]
            == "https://cdn.dummyjson.com/product-images/30/3.jpg"
        ), f'Expected {response["products"][29]["images"][2]} to be string "https://cdn.dummyjson.com/product-images/30/3.jpg", but it is not.'
        assert (
            response["products"][29]["images"][3]
            == "https://cdn.dummyjson.com/product-images/30/thumbnail.jpg"
        ), f'Expected {response["products"][29]["images"][3]} to be string "https://cdn.dummyjson.com/product-images/30/thumbnail.jpg", but it is not.'
        assert (
            response["total"] == 100
        ), f'Expected {response["total"]} to be number 100, but it is not.'
        assert (
            response["skip"] == 0
        ), f'Expected {response["skip"]} to be number 0, but it is not.'
        assert (
            response["limit"] == 30
        ), f'Expected {response["limit"]} to be number 30, but it is not.'

    @allure.story("Test GET single products")
    @allure.title("Verify the GET single products")
    @allure.description("verify the GET API response status code and data")
    @allure.severity("blocker")
    def test_get_single_products(self):
        # Act
        response_raw = requests.get(f"{base_url}/products/1")
        # Assert
        assert (
            response_raw.status_code == 200
        ), f"Expected status code 200, but got {response_raw.status_code}"
        response = response_raw.json()
        schema = {
            "type": "object",
            "properties": {
                "id": {"type": "integer"},
                "title": {"type": "string"},
                "description": {"type": "string"},
                "price": {"type": "integer"},
                "discountPercentage": {"type": "number"},
                "rating": {"type": "number"},
                "stock": {"type": "integer"},
                "brand": {"type": "string"},
                "category": {"type": "string"},
                "thumbnail": {"type": "string"},
                "images": {"type": "array", "items": {"type": "string"}},
            },
            "required": [
                "id",
                "title",
                "description",
                "price",
                "discountPercentage",
                "rating",
                "stock",
                "brand",
                "category",
                "thumbnail",
                "images",
            ],
        }
        jsonschema.validate(instance=response, schema=schema)
        keys_to_assert = [
            "id",
            "title",
            "description",
            "price",
            "discountPercentage",
            "rating",
            "stock",
            "brand",
            "category",
            "thumbnail",
            "images",
        ]
        for key in keys_to_assert:
            assert (
                key in response
            ), f"Expected {key} to be in the dictionary, but it's not."
        assert (
            response["id"] == 1
        ), f'Expected {response["id"]} to be number 1, but it is not.'
        assert (
            response["title"] == "iPhone 9"
        ), f'Expected {response["title"]} to be string "iPhone 9", but it is not.'
        assert (
            response["description"] == "An apple mobile which is nothing like apple"
        ), f'Expected {response["description"]} to be string "An apple mobile which is nothing like apple", but it is not.'
        assert (
            response["price"] == 549
        ), f'Expected {response["price"]} to be number 549, but it is not.'
        assert (
            response["discountPercentage"] == 12.96
        ), f'Expected {response["discountPercentage"]} to be number 12.96, but it is not.'
        assert (
            response["rating"] == 4.69
        ), f'Expected {response["rating"]} to be number 4.69, but it is not.'
        assert (
            response["stock"] == 94
        ), f'Expected {response["stock"]} to be number 94, but it is not.'
        assert (
            response["brand"] == "Apple"
        ), f'Expected {response["brand"]} to be string "Apple", but it is not.'
        assert (
            response["category"] == "smartphones"
        ), f'Expected {response["category"]} to be string "smartphones", but it is not.'
        assert (
            response["thumbnail"]
            == "https://cdn.dummyjson.com/product-images/1/thumbnail.jpg"
        ), f'Expected {response["thumbnail"]} to be string "https://cdn.dummyjson.com/product-images/1/thumbnail.jpg", but it is not.'
        assert isinstance(
            response["images"], list
        ), "Expected the object tobe a list, but it's not"
        assert (
            len(response["images"]) == 5
        ), "Expected the list to have length 5, but it's not"
        assert (
            response["images"][0] == "https://cdn.dummyjson.com/product-images/1/1.jpg"
        ), f'Expected {response["images"][0]} to be string "https://cdn.dummyjson.com/product-images/1/1.jpg", but it is not.'
        assert (
            response["images"][1] == "https://cdn.dummyjson.com/product-images/1/2.jpg"
        ), f'Expected {response["images"][1]} to be string "https://cdn.dummyjson.com/product-images/1/2.jpg", but it is not.'
        assert (
            response["images"][2] == "https://cdn.dummyjson.com/product-images/1/3.jpg"
        ), f'Expected {response["images"][2]} to be string "https://cdn.dummyjson.com/product-images/1/3.jpg", but it is not.'
        assert (
            response["images"][3] == "https://cdn.dummyjson.com/product-images/1/4.jpg"
        ), f'Expected {response["images"][3]} to be string "https://cdn.dummyjson.com/product-images/1/4.jpg", but it is not.'
        assert (
            response["images"][4]
            == "https://cdn.dummyjson.com/product-images/1/thumbnail.jpg"
        ), f'Expected {response["images"][4]} to be string "https://cdn.dummyjson.com/product-images/1/thumbnail.jpg", but it is not.'

    @allure.story("Test GET search product")
    @allure.title("Verify the GET search product")
    @allure.description(
        "verify the GET search product API response status code and data"
    )
    @allure.severity("blocker")
    def test_search_product(self):
        # Arrange
        product = os.getenv("PRODUCT") or config.get("API", "PRODUCT")
        # Act
        response_raw = requests.get(f"{base_url}/products/search?q={product}")
        # Assert
        assert (
            response_raw.status_code == 200
        ), f"Expected status code 200, but got {response_raw.status_code}"
        response = response_raw.json()
        schema = {
            "type": "object",
            "properties": {
                "products": {
                    "type": "array",
                    "items": {
                        "type": "object",
                        "properties": {
                            "id": {"type": "integer"},
                            "title": {"type": "string"},
                            "description": {"type": "string"},
                            "price": {"type": "integer"},
                            "discountPercentage": {"type": "number"},
                            "rating": {"type": "number"},
                            "stock": {"type": "integer"},
                            "brand": {"type": "string"},
                            "category": {"type": "string"},
                            "thumbnail": {"type": "string"},
                            "images": {"type": "array", "items": {"type": "string"}},
                        },
                        "required": [
                            "id",
                            "title",
                            "description",
                            "price",
                            "discountPercentage",
                            "rating",
                            "stock",
                            "brand",
                            "category",
                            "thumbnail",
                            "images",
                        ],
                    },
                },
                "total": {"type": "integer"},
                "skip": {"type": "integer"},
                "limit": {"type": "integer"},
            },
            "required": ["products", "total", "skip", "limit"],
        }
        jsonschema.validate(instance=response, schema=schema)
        keys_to_assert = ["products", "total", "skip", "limit"]
        for key in keys_to_assert:
            assert (
                key in response
            ), f"Expected {key} to be in the dictionary, but it's not."
        assert isinstance(
            response["products"], list
        ), "Expected the object tobe a list, but it's not"
        assert (
            len(response["products"]) == 4
        ), "Expected the list to have length 4, but it's not"
        keys_to_assert = [
            "id",
            "title",
            "description",
            "price",
            "discountPercentage",
            "rating",
            "stock",
            "brand",
            "category",
            "thumbnail",
            "images",
        ]
        for key in keys_to_assert:
            assert (
                key in response["products"][0]
            ), f"Expected {key} to be in the dictionary, but it's not."
        assert (
            response["products"][0]["id"] == 1
        ), f'Expected {response["products"][0]["id"]} to be number 1, but it is not.'
        assert (
            response["products"][0]["title"] == "iPhone 9"
        ), f'Expected {response["products"][0]["title"]} to be string "iPhone 9", but it is not.'
        assert (
            response["products"][0]["description"]
            == "An apple mobile which is nothing like apple"
        ), f'Expected {response["products"][0]["description"]} to be string "An apple mobile which is nothing like apple", but it is not.'
        assert (
            response["products"][0]["price"] == 549
        ), f'Expected {response["products"][0]["price"]} to be number 549, but it is not.'
        assert (
            response["products"][0]["discountPercentage"] == 12.96
        ), f'Expected {response["products"][0]["discountPercentage"]} to be number 12.96, but it is not.'
        assert (
            response["products"][0]["rating"] == 4.69
        ), f'Expected {response["products"][0]["rating"]} to be number 4.69, but it is not.'
        assert (
            response["products"][0]["stock"] == 94
        ), f'Expected {response["products"][0]["stock"]} to be number 94, but it is not.'
        assert (
            response["products"][0]["brand"] == "Apple"
        ), f'Expected {response["products"][0]["brand"]} to be string "Apple", but it is not.'
        assert (
            response["products"][0]["category"] == "smartphones"
        ), f'Expected {response["products"][0]["category"]} to be string "smartphones", but it is not.'
        assert (
            response["products"][0]["thumbnail"]
            == "https://cdn.dummyjson.com/product-images/1/thumbnail.jpg"
        ), f'Expected {response["products"][0]["thumbnail"]} to be string "https://cdn.dummyjson.com/product-images/1/thumbnail.jpg", but it is not.'
        assert isinstance(
            response["products"][0]["images"], list
        ), "Expected the object tobe a list, but it's not"
        assert (
            len(response["products"][0]["images"]) == 5
        ), "Expected the list to have length 5, but it's not"
        assert (
            response["products"][0]["images"][0]
            == "https://cdn.dummyjson.com/product-images/1/1.jpg"
        ), f'Expected {response["products"][0]["images"][0]} to be string "https://cdn.dummyjson.com/product-images/1/1.jpg", but it is not.'
        assert (
            response["products"][0]["images"][1]
            == "https://cdn.dummyjson.com/product-images/1/2.jpg"
        ), f'Expected {response["products"][0]["images"][1]} to be string "https://cdn.dummyjson.com/product-images/1/2.jpg", but it is not.'
        assert (
            response["products"][0]["images"][2]
            == "https://cdn.dummyjson.com/product-images/1/3.jpg"
        ), f'Expected {response["products"][0]["images"][2]} to be string "https://cdn.dummyjson.com/product-images/1/3.jpg", but it is not.'
        assert (
            response["products"][0]["images"][3]
            == "https://cdn.dummyjson.com/product-images/1/4.jpg"
        ), f'Expected {response["products"][0]["images"][3]} to be string "https://cdn.dummyjson.com/product-images/1/4.jpg", but it is not.'
        assert (
            response["products"][0]["images"][4]
            == "https://cdn.dummyjson.com/product-images/1/thumbnail.jpg"
        ), f'Expected {response["products"][0]["images"][4]} to be string "https://cdn.dummyjson.com/product-images/1/thumbnail.jpg", but it is not.'
        keys_to_assert = [
            "id",
            "title",
            "description",
            "price",
            "discountPercentage",
            "rating",
            "stock",
            "brand",
            "category",
            "thumbnail",
            "images",
        ]
        for key in keys_to_assert:
            assert (
                key in response["products"][1]
            ), f"Expected {key} to be in the dictionary, but it's not."
        assert (
            response["products"][1]["id"] == 2
        ), f'Expected {response["products"][1]["id"]} to be number 2, but it is not.'
        assert (
            response["products"][1]["title"] == "iPhone X"
        ), f'Expected {response["products"][1]["title"]} to be string "iPhone X", but it is not.'
        assert (
            response["products"][1]["description"]
            == "SIM-Free, Model A19211 6.5-inch Super Retina HD display with OLED technology A12 Bionic chip with ..."
        ), f'Expected {response["products"][1]["description"]} to be string "SIM-Free, Model A19211 6.5-inch Super Retina HD display with OLED technology A12 Bionic chip with ...", but it is not.'
        assert (
            response["products"][1]["price"] == 899
        ), f'Expected {response["products"][1]["price"]} to be number 899, but it is not.'
        assert (
            response["products"][1]["discountPercentage"] == 17.94
        ), f'Expected {response["products"][1]["discountPercentage"]} to be number 17.94, but it is not.'
        assert (
            response["products"][1]["rating"] == 4.44
        ), f'Expected {response["products"][1]["rating"]} to be number 4.44, but it is not.'
        assert (
            response["products"][1]["stock"] == 34
        ), f'Expected {response["products"][1]["stock"]} to be number 34, but it is not.'
        assert (
            response["products"][1]["brand"] == "Apple"
        ), f'Expected {response["products"][1]["brand"]} to be string "Apple", but it is not.'
        assert (
            response["products"][1]["category"] == "smartphones"
        ), f'Expected {response["products"][1]["category"]} to be string "smartphones", but it is not.'
        assert (
            response["products"][1]["thumbnail"]
            == "https://cdn.dummyjson.com/product-images/2/thumbnail.jpg"
        ), f'Expected {response["products"][1]["thumbnail"]} to be string "https://cdn.dummyjson.com/product-images/2/thumbnail.jpg", but it is not.'
        assert isinstance(
            response["products"][1]["images"], list
        ), "Expected the object tobe a list, but it's not"
        assert (
            len(response["products"][1]["images"]) == 4
        ), "Expected the list to have length 4, but it's not"
        assert (
            response["products"][1]["images"][0]
            == "https://cdn.dummyjson.com/product-images/2/1.jpg"
        ), f'Expected {response["products"][1]["images"][0]} to be string "https://cdn.dummyjson.com/product-images/2/1.jpg", but it is not.'
        assert (
            response["products"][1]["images"][1]
            == "https://cdn.dummyjson.com/product-images/2/2.jpg"
        ), f'Expected {response["products"][1]["images"][1]} to be string "https://cdn.dummyjson.com/product-images/2/2.jpg", but it is not.'
        assert (
            response["products"][1]["images"][2]
            == "https://cdn.dummyjson.com/product-images/2/3.jpg"
        ), f'Expected {response["products"][1]["images"][2]} to be string "https://cdn.dummyjson.com/product-images/2/3.jpg", but it is not.'
        assert (
            response["products"][1]["images"][3]
            == "https://cdn.dummyjson.com/product-images/2/thumbnail.jpg"
        ), f'Expected {response["products"][1]["images"][3]} to be string "https://cdn.dummyjson.com/product-images/2/thumbnail.jpg", but it is not.'
        keys_to_assert = [
            "id",
            "title",
            "description",
            "price",
            "discountPercentage",
            "rating",
            "stock",
            "brand",
            "category",
            "thumbnail",
            "images",
        ]
        for key in keys_to_assert:
            assert (
                key in response["products"][2]
            ), f"Expected {key} to be in the dictionary, but it's not."
        assert (
            response["products"][2]["id"] == 71
        ), f'Expected {response["products"][2]["id"]} to be number 71, but it is not.'
        assert (
            response["products"][2]["title"] == "Women Shoulder Bags"
        ), f'Expected {response["products"][2]["title"]} to be string "Women Shoulder Bags", but it is not.'
        assert (
            response["products"][2]["description"]
            == "LouisWill Women Shoulder Bags Long Clutches Cross Body Bags Phone Bags PU Leather Hand Bags Large Capacity Card Holders Zipper Coin Purses Fashion Crossbody Bags for Girls Ladies"
        ), f'Expected {response["products"][2]["description"]} to be string "LouisWill Women Shoulder Bags Long Clutches Cross Body Bags Phone Bags PU Leather Hand Bags Large Capacity Card Holders Zipper Coin Purses Fashion Crossbody Bags for Girls Ladies", but it is not.'
        assert (
            response["products"][2]["price"] == 46
        ), f'Expected {response["products"][2]["price"]} to be number 46, but it is not.'
        assert (
            response["products"][2]["discountPercentage"] == 14.65
        ), f'Expected {response["products"][2]["discountPercentage"]} to be number 14.65, but it is not.'
        assert (
            response["products"][2]["rating"] == 4.71
        ), f'Expected {response["products"][2]["rating"]} to be number 4.71, but it is not.'
        assert (
            response["products"][2]["stock"] == 17
        ), f'Expected {response["products"][2]["stock"]} to be number 17, but it is not.'
        assert (
            response["products"][2]["brand"] == "LouisWill"
        ), f'Expected {response["products"][2]["brand"]} to be string "LouisWill", but it is not.'
        assert (
            response["products"][2]["category"] == "womens-bags"
        ), f'Expected {response["products"][2]["category"]} to be string "womens-bags", but it is not.'
        assert (
            response["products"][2]["thumbnail"]
            == "https://cdn.dummyjson.com/product-images/71/thumbnail.jpg"
        ), f'Expected {response["products"][2]["thumbnail"]} to be string "https://cdn.dummyjson.com/product-images/71/thumbnail.jpg", but it is not.'
        assert isinstance(
            response["products"][2]["images"], list
        ), "Expected the object tobe a list, but it's not"
        assert (
            len(response["products"][2]["images"]) == 4
        ), "Expected the list to have length 4, but it's not"
        assert (
            response["products"][2]["images"][0]
            == "https://cdn.dummyjson.com/product-images/71/1.jpg"
        ), f'Expected {response["products"][2]["images"][0]} to be string "https://cdn.dummyjson.com/product-images/71/1.jpg", but it is not.'
        assert (
            response["products"][2]["images"][1]
            == "https://cdn.dummyjson.com/product-images/71/2.jpg"
        ), f'Expected {response["products"][2]["images"][1]} to be string "https://cdn.dummyjson.com/product-images/71/2.jpg", but it is not.'
        assert (
            response["products"][2]["images"][2]
            == "https://cdn.dummyjson.com/product-images/71/3.webp"
        ), f'Expected {response["products"][2]["images"][2]} to be string "https://cdn.dummyjson.com/product-images/71/3.webp", but it is not.'
        assert (
            response["products"][2]["images"][3]
            == "https://cdn.dummyjson.com/product-images/71/thumbnail.jpg"
        ), f'Expected {response["products"][2]["images"][3]} to be string "https://cdn.dummyjson.com/product-images/71/thumbnail.jpg", but it is not.'
        keys_to_assert = [
            "id",
            "title",
            "description",
            "price",
            "discountPercentage",
            "rating",
            "stock",
            "brand",
            "category",
            "thumbnail",
            "images",
        ]
        for key in keys_to_assert:
            assert (
                key in response["products"][3]
            ), f"Expected {key} to be in the dictionary, but it's not."
        assert (
            response["products"][3]["id"] == 86
        ), f'Expected {response["products"][3]["id"]} to be number 86, but it is not.'
        assert (
            response["products"][3]["title"] == "Bluetooth Aux"
        ), f'Expected {response["products"][3]["title"]} to be string "Bluetooth Aux", but it is not.'
        assert (
            response["products"][3]["description"]
            == "Bluetooth Aux Bluetooth Car Aux Car Bluetooth Transmitter Aux Audio Receiver Handfree Car Bluetooth Music Receiver Universal 3.5mm Streaming A2DP Wireless Auto AUX Audio Adapter With Mic For Phone MP3"
        ), f'Expected {response["products"][3]["description"]} to be string "Bluetooth Aux Bluetooth Car Aux Car Bluetooth Transmitter Aux Audio Receiver Handfree Car Bluetooth Music Receiver Universal 3.5mm Streaming A2DP Wireless Auto AUX Audio Adapter With Mic For Phone MP3", but it is not.'
        assert (
            response["products"][3]["price"] == 25
        ), f'Expected {response["products"][3]["price"]} to be number 25, but it is not.'
        assert (
            response["products"][3]["discountPercentage"] == 10.56
        ), f'Expected {response["products"][3]["discountPercentage"]} to be number 10.56, but it is not.'
        assert (
            response["products"][3]["rating"] == 4.57
        ), f'Expected {response["products"][3]["rating"]} to be number 4.57, but it is not.'
        assert (
            response["products"][3]["stock"] == 22
        ), f'Expected {response["products"][3]["stock"]} to be number 22, but it is not.'
        assert (
            response["products"][3]["brand"] == "Car Aux"
        ), f'Expected {response["products"][3]["brand"]} to be string "Car Aux", but it is not.'
        assert (
            response["products"][3]["category"] == "automotive"
        ), f'Expected {response["products"][3]["category"]} to be string "automotive", but it is not.'
        assert (
            response["products"][3]["thumbnail"]
            == "https://cdn.dummyjson.com/product-images/86/thumbnail.jpg"
        ), f'Expected {response["products"][3]["thumbnail"]} to be string "https://cdn.dummyjson.com/product-images/86/thumbnail.jpg", but it is not.'
        assert isinstance(
            response["products"][3]["images"], list
        ), "Expected the object tobe a list, but it's not"
        assert (
            len(response["products"][3]["images"]) == 5
        ), "Expected the list to have length 5, but it's not"
        assert (
            response["products"][3]["images"][0]
            == "https://cdn.dummyjson.com/product-images/86/1.jpg"
        ), f'Expected {response["products"][3]["images"][0]} to be string "https://cdn.dummyjson.com/product-images/86/1.jpg", but it is not.'
        assert (
            response["products"][3]["images"][1]
            == "https://cdn.dummyjson.com/product-images/86/2.webp"
        ), f'Expected {response["products"][3]["images"][1]} to be string "https://cdn.dummyjson.com/product-images/86/2.webp", but it is not.'
        assert (
            response["products"][3]["images"][2]
            == "https://cdn.dummyjson.com/product-images/86/3.jpg"
        ), f'Expected {response["products"][3]["images"][2]} to be string "https://cdn.dummyjson.com/product-images/86/3.jpg", but it is not.'
        assert (
            response["products"][3]["images"][3]
            == "https://cdn.dummyjson.com/product-images/86/4.jpg"
        ), f'Expected {response["products"][3]["images"][3]} to be string "https://cdn.dummyjson.com/product-images/86/4.jpg", but it is not.'
        assert (
            response["products"][3]["images"][4]
            == "https://cdn.dummyjson.com/product-images/86/thumbnail.jpg"
        ), f'Expected {response["products"][3]["images"][4]} to be string "https://cdn.dummyjson.com/product-images/86/thumbnail.jpg", but it is not.'
        assert (
            response["total"] == 4
        ), f'Expected {response["total"]} to be number 4, but it is not.'
        assert (
            response["skip"] == 0
        ), f'Expected {response["skip"]} to be number 0, but it is not.'
        assert (
            response["limit"] == 4
        ), f'Expected {response["limit"]} to be number 4, but it is not.'

    @allure.story("Test GET API limit products")
    @allure.title("Verify the GET API limit products")
    @allure.description(
        "verify the GET API limit products response status code and data"
    )
    @allure.severity("blocker")
    def test_limit_products(self):
        # Arrange
        limit = os.getenv("LIMIT")

        # Act
        response_raw = requests.get(
            f"{base_url}/products?limit={limit}&skip={limit}&select=title,price"
        )

        # Assert
        assert (
            response_raw.status_code == 200
        ), f"Expected status code 200, but got {response_raw.status_code}"
        response = response_raw.json()
        schema = {
            "type": "object",
            "properties": {
                "products": {
                    "type": "array",
                    "items": {
                        "type": "object",
                        "properties": {
                            "id": {"type": "integer"},
                            "title": {"type": "string"},
                            "price": {"type": "integer"},
                        },
                        "required": ["id", "title", "price"],
                    },
                },
                "total": {"type": "integer"},
                "skip": {"type": "integer"},
                "limit": {"type": "integer"},
            },
            "required": ["products", "total", "skip", "limit"],
        }
        jsonschema.validate(instance=response, schema=schema)
        keys_to_assert = ["products", "total", "skip", "limit"]
        for key in keys_to_assert:
            assert (
                key in response
            ), f"Expected {key} to be in the dictionary, but it's not."
        assert isinstance(
            response["products"], list
        ), "Expected the object tobe a list, but it's not"
        assert (
            len(response["products"]) == 10
        ), "Expected the list to have length 10, but it's not"
        keys_to_assert = ["id", "title", "price"]
        for key in keys_to_assert:
            assert (
                key in response["products"][0]
            ), f"Expected {key} to be in the dictionary, but it's not."
        assert (
            response["products"][0]["id"] == 11
        ), f'Expected {response["products"][0]["id"]} to be number 11, but it is not.'
        assert (
            response["products"][0]["title"] == "perfume Oil"
        ), f'Expected {response["products"][0]["title"]} to be string "perfume Oil", but it is not.'
        assert (
            response["products"][0]["price"] == 13
        ), f'Expected {response["products"][0]["price"]} to be number 13, but it is not.'
        keys_to_assert = ["id", "title", "price"]
        for key in keys_to_assert:
            assert (
                key in response["products"][1]
            ), f"Expected {key} to be in the dictionary, but it's not."
        assert (
            response["products"][1]["id"] == 12
        ), f'Expected {response["products"][1]["id"]} to be number 12, but it is not.'
        assert (
            response["products"][1]["title"] == "Brown Perfume"
        ), f'Expected {response["products"][1]["title"]} to be string "Brown Perfume", but it is not.'
        assert (
            response["products"][1]["price"] == 40
        ), f'Expected {response["products"][1]["price"]} to be number 40, but it is not.'
        keys_to_assert = ["id", "title", "price"]
        for key in keys_to_assert:
            assert (
                key in response["products"][2]
            ), f"Expected {key} to be in the dictionary, but it's not."
        assert (
            response["products"][2]["id"] == 13
        ), f'Expected {response["products"][2]["id"]} to be number 13, but it is not.'
        assert (
            response["products"][2]["title"] == "Fog Scent Xpressio Perfume"
        ), f'Expected {response["products"][2]["title"]} to be string "Fog Scent Xpressio Perfume", but it is not.'
        assert (
            response["products"][2]["price"] == 13
        ), f'Expected {response["products"][2]["price"]} to be number 13, but it is not.'
        keys_to_assert = ["id", "title", "price"]
        for key in keys_to_assert:
            assert (
                key in response["products"][3]
            ), f"Expected {key} to be in the dictionary, but it's not."
        assert (
            response["products"][3]["id"] == 14
        ), f'Expected {response["products"][3]["id"]} to be number 14, but it is not.'
        assert (
            response["products"][3]["title"] == "Non-Alcoholic Concentrated Perfume Oil"
        ), f'Expected {response["products"][3]["title"]} to be string "Non-Alcoholic Concentrated Perfume Oil", but it is not.'
        assert (
            response["products"][3]["price"] == 120
        ), f'Expected {response["products"][3]["price"]} to be number 120, but it is not.'
        keys_to_assert = ["id", "title", "price"]
        for key in keys_to_assert:
            assert (
                key in response["products"][4]
            ), f"Expected {key} to be in the dictionary, but it's not."
        assert (
            response["products"][4]["id"] == 15
        ), f'Expected {response["products"][4]["id"]} to be number 15, but it is not.'
        assert (
            response["products"][4]["title"] == "Eau De Perfume Spray"
        ), f'Expected {response["products"][4]["title"]} to be string "Eau De Perfume Spray", but it is not.'
        assert (
            response["products"][4]["price"] == 30
        ), f'Expected {response["products"][4]["price"]} to be number 30, but it is not.'
        keys_to_assert = ["id", "title", "price"]
        for key in keys_to_assert:
            assert (
                key in response["products"][5]
            ), f"Expected {key} to be in the dictionary, but it's not."
        assert (
            response["products"][5]["id"] == 16
        ), f'Expected {response["products"][5]["id"]} to be number 16, but it is not.'
        assert (
            response["products"][5]["title"] == "Hyaluronic Acid Serum"
        ), f'Expected {response["products"][5]["title"]} to be string "Hyaluronic Acid Serum", but it is not.'
        assert (
            response["products"][5]["price"] == 19
        ), f'Expected {response["products"][5]["price"]} to be number 19, but it is not.'
        keys_to_assert = ["id", "title", "price"]
        for key in keys_to_assert:
            assert (
                key in response["products"][6]
            ), f"Expected {key} to be in the dictionary, but it's not."
        assert (
            response["products"][6]["id"] == 17
        ), f'Expected {response["products"][6]["id"]} to be number 17, but it is not.'
        assert (
            response["products"][6]["title"] == "Tree Oil 30ml"
        ), f'Expected {response["products"][6]["title"]} to be string "Tree Oil 30ml", but it is not.'
        assert (
            response["products"][6]["price"] == 12
        ), f'Expected {response["products"][6]["price"]} to be number 12, but it is not.'
        keys_to_assert = ["id", "title", "price"]
        for key in keys_to_assert:
            assert (
                key in response["products"][7]
            ), f"Expected {key} to be in the dictionary, but it's not."
        assert (
            response["products"][7]["id"] == 18
        ), f'Expected {response["products"][7]["id"]} to be number 18, but it is not.'
        assert (
            response["products"][7]["title"] == "Oil Free Moisturizer 100ml"
        ), f'Expected {response["products"][7]["title"]} to be string "Oil Free Moisturizer 100ml", but it is not.'
        assert (
            response["products"][7]["price"] == 40
        ), f'Expected {response["products"][7]["price"]} to be number 40, but it is not.'
        keys_to_assert = ["id", "title", "price"]
        for key in keys_to_assert:
            assert (
                key in response["products"][8]
            ), f"Expected {key} to be in the dictionary, but it's not."
        assert (
            response["products"][8]["id"] == 19
        ), f'Expected {response["products"][8]["id"]} to be number 19, but it is not.'
        assert (
            response["products"][8]["title"] == "Skin Beauty Serum."
        ), f'Expected {response["products"][8]["title"]} to be string "Skin Beauty Serum.", but it is not.'
        assert (
            response["products"][8]["price"] == 46
        ), f'Expected {response["products"][8]["price"]} to be number 46, but it is not.'
        keys_to_assert = ["id", "title", "price"]
        for key in keys_to_assert:
            assert (
                key in response["products"][9]
            ), f"Expected {key} to be in the dictionary, but it's not."
        assert (
            response["products"][9]["id"] == 20
        ), f'Expected {response["products"][9]["id"]} to be number 20, but it is not.'
        assert (
            response["products"][9]["title"] == "Freckle Treatment Cream- 15gm"
        ), f'Expected {response["products"][9]["title"]} to be string "Freckle Treatment Cream- 15gm", but it is not.'
        assert (
            response["products"][9]["price"] == 70
        ), f'Expected {response["products"][9]["price"]} to be number 70, but it is not.'
        assert (
            response["total"] == 100
        ), f'Expected {response["total"]} to be number 100, but it is not.'
        assert (
            response["skip"] == 10
        ), f'Expected {response["skip"]} to be number 10, but it is not.'
        assert (
            response["limit"] == 10
        ), f'Expected {response["limit"]} to be number 10, but it is not.'

    @allure.story("Test GET categories")
    @allure.title("Verify the get categories API")
    @allure.description("verify the GET categories API response status code and data")
    @allure.severity("blocker")
    def test_get_categories(self):
        # Arrange
        # Act
        response_raw = requests.get(f"{base_url}/products/categories")

        # Assert
        assert (
            response_raw.status_code == 200
        ), f"Expected status code 200, but got {response_raw.status_code}"
        response = response_raw.json()
        schema = {"type": "array", "items": {"type": "string"}}
        jsonschema.validate(instance=response, schema=schema)
        assert (
            response[0] == "smartphones"
        ), f'Expected {response[0]} to be string "smartphones", but it is not.'
        assert (
            response[1] == "laptops"
        ), f'Expected {response[1]} to be string "laptops", but it is not.'
        assert (
            response[2] == "fragrances"
        ), f'Expected {response[2]} to be string "fragrances", but it is not.'
        assert (
            response[3] == "skincare"
        ), f'Expected {response[3]} to be string "skincare", but it is not.'
        assert (
            response[4] == "groceries"
        ), f'Expected {response[4]} to be string "groceries", but it is not.'
        assert (
            response[5] == "home-decoration"
        ), f'Expected {response[5]} to be string "home-decoration", but it is not.'
        assert (
            response[6] == "furniture"
        ), f'Expected {response[6]} to be string "furniture", but it is not.'
        assert (
            response[7] == "tops"
        ), f'Expected {response[7]} to be string "tops", but it is not.'
        assert (
            response[8] == "womens-dresses"
        ), f'Expected {response[8]} to be string "womens-dresses", but it is not.'
        assert (
            response[9] == "womens-shoes"
        ), f'Expected {response[9]} to be string "womens-shoes", but it is not.'
        assert (
            response[10] == "mens-shirts"
        ), f'Expected {response[10]} to be string "mens-shirts", but it is not.'
        assert (
            response[11] == "mens-shoes"
        ), f'Expected {response[11]} to be string "mens-shoes", but it is not.'
        assert (
            response[12] == "mens-watches"
        ), f'Expected {response[12]} to be string "mens-watches", but it is not.'
        assert (
            response[13] == "womens-watches"
        ), f'Expected {response[13]} to be string "womens-watches", but it is not.'
        assert (
            response[14] == "womens-bags"
        ), f'Expected {response[14]} to be string "womens-bags", but it is not.'
        assert (
            response[15] == "womens-jewellery"
        ), f'Expected {response[15]} to be string "womens-jewellery", but it is not.'
        assert (
            response[16] == "sunglasses"
        ), f'Expected {response[16]} to be string "sunglasses", but it is not.'
        assert (
            response[17] == "automotive"
        ), f'Expected {response[17]} to be string "automotive", but it is not.'
        assert (
            response[18] == "motorcycle"
        ), f'Expected {response[18]} to be string "motorcycle", but it is not.'
        assert (
            response[19] == "lighting"
        ), f'Expected {response[19]} to be string "lighting", but it is not.'


if __name__ == "__main__":
    pytest.main([__file__])
