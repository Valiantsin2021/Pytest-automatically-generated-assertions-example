import requests
# import configparser
import pytest
import allure
import jsonschema
import os
from dotenv import load_dotenv

load_dotenv()

token = ""
base_url = os.getenv("BASE_URL")
user = os.getenv("USER")
password = os.getenv("PASSWORD")
headers = {"Content-Type": "application/json"}


@allure.feature("Test Dummy JSON API")
class TestClass:
    @allure.story("Test POST login")
    @allure.title("Verify the POST login")
    @allure.description("verify the POST login API response status code and data")
    @allure.severity("blocker")
    def test_login(self):
        # Arrange
        global user, password, token
        # Act
        response_raw = requests.post(
            f"{base_url}/auth/login",
            json={"username": "kminchelle", "password": "0lelplR"},
            headers=headers,
        )
        # Assert
        assert (
            response_raw.status_code == 200
        ), f"Expected status code 200, but got {response_raw.status_code} {response_raw.content}"
        response = response_raw.json()
        schema = {
            "type": "object",
            "properties": {
                "id": {"type": "integer"},
                "username": {"type": "string"},
                "email": {"type": "string"},
                "firstName": {"type": "string"},
                "lastName": {"type": "string"},
                "gender": {"type": "string"},
                "image": {"type": "string"},
                "token": {"type": "string"},
            },
            "required": [
                "id",
                "username",
                "email",
                "firstName",
                "lastName",
                "gender",
                "image",
                "token",
            ],
        }
        try:
            jsonschema.validate(instance=response, schema=schema)
        except jsonschema.exceptions.ValidationError as e:
            assert False, f"Schema validation failed: {e}"
        assert True
        keys_to_assert = [
            "id",
            "username",
            "email",
            "firstName",
            "lastName",
            "gender",
            "image",
            "token",
        ]
        for key in keys_to_assert:
            assert (
                key in response
            ), f"Expected {key} to be in the dictionary, but it's not."
        assert (
            response["id"] == 15
        ), f'Expected {response["id"]} to be number 15, but it is not.'
        assert (
            response["username"] == "kminchelle"
        ), f'Expected {response["username"]} to be string "kminchelle", but it is not.'
        assert (
            response["email"] == "kminchelle@qq.com"
        ), f'Expected {response["email"]} to be string "kminchelle@qq.com", but it is not.'
        assert (
            response["firstName"] == "Jeanne"
        ), f'Expected {response["firstName"]} to be string "Jeanne", but it is not.'
        assert (
            response["lastName"] == "Halvorson"
        ), f'Expected {response["lastName"]} to be string "Halvorson", but it is not.'
        assert (
            response["gender"] == "female"
        ), f'Expected {response["gender"]} to be string "female", but it is not.'
        assert (
            response["image"] == "https://robohash.org/Jeanne.png?set=set4"
        ), f'Expected {response["image"]} to be string "https://robohash.org/Jeanne.png?set=set4", but it is not.'
        assert isinstance(
            response["token"], str
        ), f'Expected {response["token"]} to be string , but it is not.'
        token = response["token"]

    @allure.story("Test GET all products")
    @allure.title("Verify the GET products")
    @allure.description("verify the GET API response status code and data")
    @allure.severity("blocker")
    def test_token(self):
        # Arrange
        global token
        auth_headers = {"Authorization": f"Bearer {token}"}
        # Act
        response_raw = requests.get(
            f"{base_url}/auth/me",
            headers=auth_headers,
        )
        # Assert
        assert (
            response_raw.status_code == 200
        ), f"Expected status code 200, but got {response_raw.status_code} {response_raw.content}"
        response = response_raw.json()
        schema = {
            "type": "object",
            "properties": {
                "id": {"type": "integer"},
                "firstName": {"type": "string"},
                "lastName": {"type": "string"},
                "maidenName": {"type": "string"},
                "age": {"type": "integer"},
                "gender": {"type": "string"},
                "email": {"type": "string"},
                "phone": {"type": "string"},
                "username": {"type": "string"},
                "password": {"type": "string"},
                "birthDate": {"type": "string"},
                "image": {"type": "string"},
                "bloodGroup": {"type": "string"},
                "height": {"type": "integer"},
                "weight": {"type": "number"},
                "eyeColor": {"type": "string"},
                "hair": {
                    "type": "object",
                    "properties": {
                        "color": {"type": "string"},
                        "type": {"type": "string"},
                    },
                    "required": ["color", "type"],
                },
                "domain": {"type": "string"},
                "ip": {"type": "string"},
                "address": {
                    "type": "object",
                    "properties": {
                        "address": {"type": "string"},
                        "city": {"type": "string"},
                        "coordinates": {
                            "type": "object",
                            "properties": {
                                "lat": {"type": "number"},
                                "lng": {"type": "number"},
                            },
                            "required": ["lat", "lng"],
                        },
                        "postalCode": {"type": "string"},
                        "state": {"type": "string"},
                    },
                    "required": [
                        "address",
                        "city",
                        "coordinates",
                        "postalCode",
                        "state",
                    ],
                },
                "macAddress": {"type": "string"},
                "university": {"type": "string"},
                "bank": {
                    "type": "object",
                    "properties": {
                        "cardExpire": {"type": "string"},
                        "cardNumber": {"type": "string"},
                        "cardType": {"type": "string"},
                        "currency": {"type": "string"},
                        "iban": {"type": "string"},
                    },
                    "required": [
                        "cardExpire",
                        "cardNumber",
                        "cardType",
                        "currency",
                        "iban",
                    ],
                },
                "company": {
                    "type": "object",
                    "properties": {
                        "address": {
                            "type": "object",
                            "properties": {
                                "address": {"type": "string"},
                                "city": {"type": "string"},
                                "coordinates": {
                                    "type": "object",
                                    "properties": {
                                        "lat": {"type": "number"},
                                        "lng": {"type": "number"},
                                    },
                                    "required": ["lat", "lng"],
                                },
                                "postalCode": {"type": "string"},
                                "state": {"type": "string"},
                            },
                            "required": [
                                "address",
                                "city",
                                "coordinates",
                                "postalCode",
                                "state",
                            ],
                        },
                        "department": {"type": "string"},
                        "name": {"type": "string"},
                        "title": {"type": "string"},
                    },
                    "required": ["address", "department", "name", "title"],
                },
                "ein": {"type": "string"},
                "ssn": {"type": "string"},
                "userAgent": {"type": "string"},
                "crypto": {
                    "type": "object",
                    "properties": {
                        "coin": {"type": "string"},
                        "wallet": {"type": "string"},
                        "network": {"type": "string"},
                    },
                    "required": ["coin", "wallet", "network"],
                },
            },
            "required": [
                "id",
                "firstName",
                "lastName",
                "maidenName",
                "age",
                "gender",
                "email",
                "phone",
                "username",
                "password",
                "birthDate",
                "image",
                "bloodGroup",
                "height",
                "weight",
                "eyeColor",
                "hair",
                "domain",
                "ip",
                "address",
                "macAddress",
                "university",
                "bank",
                "company",
                "ein",
                "ssn",
                "userAgent",
                "crypto",
            ],
        }
        try:
            jsonschema.validate(instance=response, schema=schema)
        except jsonschema.exceptions.ValidationError as e:
            assert False, f"Schema validation failed: {e}"
        assert True
        keys_to_assert = [
            "id",
            "firstName",
            "lastName",
            "maidenName",
            "age",
            "gender",
            "email",
            "phone",
            "username",
            "password",
            "birthDate",
            "image",
            "bloodGroup",
            "height",
            "weight",
            "eyeColor",
            "hair",
            "domain",
            "ip",
            "address",
            "macAddress",
            "university",
            "bank",
            "company",
            "ein",
            "ssn",
            "userAgent",
            "crypto",
        ]
        for key in keys_to_assert:
            assert (
                key in response
            ), f"Expected {key} to be in the dictionary, but it's not."
        assert (
            response["id"] == 15
        ), f'Expected {response["id"]} to be number 15, but it is not.'
        assert (
            response["firstName"] == "Jeanne"
        ), f'Expected {response["firstName"]} to be string "Jeanne", but it is not.'
        assert (
            response["lastName"] == "Halvorson"
        ), f'Expected {response["lastName"]} to be string "Halvorson", but it is not.'
        assert (
            response["maidenName"] == "Cummerata"
        ), f'Expected {response["maidenName"]} to be string "Cummerata", but it is not.'
        assert (
            response["age"] == 26
        ), f'Expected {response["age"]} to be number 26, but it is not.'
        assert (
            response["gender"] == "female"
        ), f'Expected {response["gender"]} to be string "female", but it is not.'
        assert (
            response["email"] == "kminchelle@qq.com"
        ), f'Expected {response["email"]} to be string "kminchelle@qq.com", but it is not.'
        assert (
            response["phone"] == "+86 581 108 7855"
        ), f'Expected {response["phone"]} to be string "+86 581 108 7855", but it is not.'
        assert (
            response["username"] == "kminchelle"
        ), f'Expected {response["username"]} to be string "kminchelle", but it is not.'
        assert (
            response["password"] == "0lelplR"
        ), f'Expected {response["password"]} to be string "0lelplR", but it is not.'
        assert (
            response["birthDate"] == "1996-02-02"
        ), f'Expected {response["birthDate"]} to be string "1996-02-02", but it is not.'
        assert (
            response["image"] == "https://robohash.org/Jeanne.png?set=set4"
        ), f'Expected {response["image"]} to be string "https://robohash.org/Jeanne.png?set=set4", but it is not.'
        assert (
            response["bloodGroup"] == "A+"
        ), f'Expected {response["bloodGroup"]} to be string "A+", but it is not.'
        assert (
            response["height"] == 176
        ), f'Expected {response["height"]} to be number 176, but it is not.'
        assert (
            response["weight"] == 45.7
        ), f'Expected {response["weight"]} to be number 45.7, but it is not.'
        assert (
            response["eyeColor"] == "Amber"
        ), f'Expected {response["eyeColor"]} to be string "Amber", but it is not.'
        keys_to_assert = ["color", "type"]
        for key in keys_to_assert:
            assert (
                key in response["hair"]
            ), f"Expected {key} to be in the dictionary, but it's not."
        assert (
            response["hair"]["color"] == "Blond"
        ), f'Expected {response["hair"]["color"]} to be string "Blond", but it is not.'
        assert (
            response["hair"]["type"] == "Straight"
        ), f'Expected {response["hair"]["type"]} to be string "Straight", but it is not.'
        assert (
            response["domain"] == "google.co.uk"
        ), f'Expected {response["domain"]} to be string "google.co.uk", but it is not.'
        assert (
            response["ip"] == "78.43.74.226"
        ), f'Expected {response["ip"]} to be string "78.43.74.226", but it is not.'
        keys_to_assert = ["address", "city", "coordinates", "postalCode", "state"]
        for key in keys_to_assert:
            assert (
                key in response["address"]
            ), f"Expected {key} to be in the dictionary, but it's not."
        assert (
            response["address"]["address"] == "4 Old Colony Way"
        ), f'Expected {response["address"]["address"]} to be string "4 Old Colony Way", but it is not.'
        assert (
            response["address"]["city"] == "Yarmouth"
        ), f'Expected {response["address"]["city"]} to be string "Yarmouth", but it is not.'
        keys_to_assert = ["lat", "lng"]
        for key in keys_to_assert:
            assert (
                key in response["address"]["coordinates"]
            ), f"Expected {key} to be in the dictionary, but it's not."
        assert (
            response["address"]["coordinates"]["lat"] == 41.697168
        ), f'Expected {response["address"]["coordinates"]["lat"]} to be number 41.697168, but it is not.'
        assert (
            response["address"]["coordinates"]["lng"] == -70.189992
        ), f'Expected {response["address"]["coordinates"]["lng"]} to be number -70.189992, but it is not.'
        assert (
            response["address"]["postalCode"] == "02664"
        ), f'Expected {response["address"]["postalCode"]} to be string "02664", but it is not.'
        assert (
            response["address"]["state"] == "MA"
        ), f'Expected {response["address"]["state"]} to be string "MA", but it is not.'
        assert (
            response["macAddress"] == "D9:DB:D9:5A:01:09"
        ), f'Expected {response["macAddress"]} to be string "D9:DB:D9:5A:01:09", but it is not.'
        assert (
            response["university"] == "Donghua University, Shanghai"
        ), f'Expected {response["university"]} to be string "Donghua University, Shanghai", but it is not.'
        keys_to_assert = ["cardExpire", "cardNumber", "cardType", "currency", "iban"]
        for key in keys_to_assert:
            assert (
                key in response["bank"]
            ), f"Expected {key} to be in the dictionary, but it's not."
        assert (
            response["bank"]["cardExpire"] == "10/23"
        ), f'Expected {response["bank"]["cardExpire"]} to be string "10/23", but it is not.'
        assert (
            response["bank"]["cardNumber"] == "3588859507772914"
        ), f'Expected {response["bank"]["cardNumber"]} to be string "3588859507772914", but it is not.'
        assert (
            response["bank"]["cardType"] == "jcb"
        ), f'Expected {response["bank"]["cardType"]} to be string "jcb", but it is not.'
        assert (
            response["bank"]["currency"] == "Yuan Renminbi"
        ), f'Expected {response["bank"]["currency"]} to be string "Yuan Renminbi", but it is not.'
        assert (
            response["bank"]["iban"] == "FO12 1440 0396 8902 56"
        ), f'Expected {response["bank"]["iban"]} to be string "FO12 1440 0396 8902 56", but it is not.'
        keys_to_assert = ["address", "department", "name", "title"]
        for key in keys_to_assert:
            assert (
                key in response["company"]
            ), f"Expected {key} to be in the dictionary, but it's not."
        keys_to_assert = ["address", "city", "coordinates", "postalCode", "state"]
        for key in keys_to_assert:
            assert (
                key in response["company"]["address"]
            ), f"Expected {key} to be in the dictionary, but it's not."
        assert (
            response["company"]["address"]["address"] == "22572 Toreador Drive"
        ), f'Expected {response["company"]["address"]["address"]} to be string "22572 Toreador Drive", but it is not.'
        assert (
            response["company"]["address"]["city"] == "Salinas"
        ), f'Expected {response["company"]["address"]["city"]} to be string "Salinas", but it is not.'
        keys_to_assert = ["lat", "lng"]
        for key in keys_to_assert:
            assert (
                key in response["company"]["address"]["coordinates"]
            ), f"Expected {key} to be in the dictionary, but it's not."
        assert (
            response["company"]["address"]["coordinates"]["lat"] == 36.602449
        ), f'Expected {response["company"]["address"]["coordinates"]["lat"]} to be number 36.602449, but it is not.'
        assert (
            response["company"]["address"]["coordinates"]["lng"] == -121.699071
        ), f'Expected {response["company"]["address"]["coordinates"]["lng"]} to be number -121.699071, but it is not.'
        assert (
            response["company"]["address"]["postalCode"] == "93908"
        ), f'Expected {response["company"]["address"]["postalCode"]} to be string "93908", but it is not.'
        assert (
            response["company"]["address"]["state"] == "CA"
        ), f'Expected {response["company"]["address"]["state"]} to be string "CA", but it is not.'
        assert (
            response["company"]["department"] == "Marketing"
        ), f'Expected {response["company"]["department"]} to be string "Marketing", but it is not.'
        assert (
            response["company"]["name"] == "Hahn-MacGyver"
        ), f'Expected {response["company"]["name"]} to be string "Hahn-MacGyver", but it is not.'
        assert (
            response["company"]["title"] == "Software Test Engineer IV"
        ), f'Expected {response["company"]["title"]} to be string "Software Test Engineer IV", but it is not.'
        assert (
            response["ein"] == "62-0561095"
        ), f'Expected {response["ein"]} to be string "62-0561095", but it is not.'
        assert (
            response["ssn"] == "855-43-8639"
        ), f'Expected {response["ssn"]} to be string "855-43-8639", but it is not.'
        assert (
            response["userAgent"]
            == "Mozilla/5.0 (X11; Linux i686) AppleWebKit/534.24 (KHTML, like Gecko) Chrome/11.0.696.14 Safari/534.24"
        ), f'Expected {response["userAgent"]} to be string "Mozilla/5.0 (X11; Linux i686) AppleWebKit/534.24 (KHTML, like Gecko) Chrome/11.0.696.14 Safari/534.24", but it is not.'
        keys_to_assert = ["coin", "wallet", "network"]
        for key in keys_to_assert:
            assert (
                key in response["crypto"]
            ), f"Expected {key} to be in the dictionary, but it's not."
        assert (
            response["crypto"]["coin"] == "Bitcoin"
        ), f'Expected {response["crypto"]["coin"]} to be string "Bitcoin", but it is not.'
        assert (
            response["crypto"]["wallet"] == "0xb9fc1004bfe7702de522516cf34a5da41c4ef2b5"
        ), f'Expected {response["crypto"]["wallet"]} to be string "0xb9fc1004bfe7702de522516cf34a5da41c4ef2b5", but it is not.'
        assert (
            response["crypto"]["network"] == "Ethereum (ERC20)"
        ), f'Expected {response["crypto"]["network"]} to be string "Ethereum (ERC20)", but it is not.'


if __name__ == "__main__":
    pytest.main([__file__])
