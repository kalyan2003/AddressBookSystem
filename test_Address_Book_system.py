import pytest
from main import (
    validate_first_and_last_name,
    validate_address,
    validate_city,
    validate_zip_code,
    validate_phone_number,
    validate_email_id
)

@pytest.mark.parametrize("first_name, last_name, address, city, zip_code, phone, email, expected", [
    ("John", "Doe", "123MainRoadX", "Hyderabad", "500001", "9876543210", "john.doe@example.com",
     (True, True, True, True, True, True, True)),
    ("john", "Doe", "123MainRoadX", "Hyderabad", "500001", "9876543210", "john.doe@example.com",
     (False, True, True, True, True, True, True)),
    ("John", "Do", "123MainRoadX", "Hyderabad", "500001", "9876543210", "john.doe@example.com",
     (True, False, True, True, True, True, True)),
    ("John", "Doe", "123Main", "Hyderabad", "500001", "9876543210", "john.doe@example.com",
     (True, True, False, True, True, True, True)),
    ("John", "Doe", "123MainRoadX", "Hyd3rabad", "500001", "9876543210", "john.doe@example.com",
     (True, True, True, False, True, True, True)),
    ("John", "Doe", "123MainRoadX", "Hyderabad", "5000", "9876543210", "john.doe@example.com",
     (True, True, True, True, False, True, True)),
    ("John", "Doe", "123MainRoadX", "Hyderabad", "500001", "1234567890", "john.doe@example.com",
     (True, True, True, True, True, False, True)),
    ("John", "Doe", "123MainRoadX", "Hyderabad", "500001", "9876543210", "johndoe.com",
     (True, True, True, True, True, True, False)),
])
def test_validate_the_input(first_name, last_name, address, city, zip_code, phone, email, expected):
    exp_fn, exp_ln, exp_addr, exp_city, exp_zip, exp_phone, exp_email = expected

    assert validate_first_and_last_name(first_name) == exp_fn
    assert validate_first_and_last_name(last_name) == exp_ln
    assert validate_address(address) == exp_addr
    assert validate_city(city) == exp_city
    assert validate_zip_code(zip_code) == exp_zip
    assert validate_phone_number(phone) == exp_phone
    assert validate_email_id(email) == exp_email
