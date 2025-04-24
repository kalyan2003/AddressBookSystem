import pytest
from validators_utils import (
    validate_first_name,
    validate_last_name,
    validate_address,
    validate_city,
    validate_state,
    validate_zip_code,
    validate_phone,
    validate_email
)
from Address_book import AddressBook
from schema import Contact
from Address_Book_Management import AddressBookSystem


# Test Validators
@pytest.mark.parametrize("first_name, expected", [
    ("John", True),
    ("john", False),
    ("J", False),
    ("Jo", True),
])
def test_validate_first_name(first_name, expected):
    result = validate_first_name(first_name)
    assert (result is not None) == expected


@pytest.mark.parametrize("last_name, expected", [
    ("Doe", True),
    ("doe", False),
    ("D", False),
    ("Do", True),
])
def test_validate_last_name(last_name, expected):
    result = validate_last_name(last_name)
    assert (result is not None) == expected


@pytest.mark.parametrize("address, expected", [
    ("123MainRoadX", True),
    ("123", False),
    ("Main St, 456", True),
])
def test_validate_address(address, expected):
    result = validate_address(address)
    assert (result is not None) == expected


@pytest.mark.parametrize("city, expected", [
    ("Hyderabad", True),
    ("Hyder@bad", False),
    ("", False),
])
def test_validate_city(city, expected):
    result = validate_city(city)
    assert (result is not None) == expected


@pytest.mark.parametrize("state, expected", [
    ("Telangana", True),
    ("Telang@na", False),
    ("", False),
])
def test_validate_state(state, expected):
    result = validate_state(state)
    assert (result is not None) == expected


@pytest.mark.parametrize("zip_code, expected", [
    ("500001", True),
    ("5000", False),
    ("abcd", False),
])
def test_validate_zip_code(zip_code, expected):
    result = validate_zip_code(zip_code)
    assert (result is not None) == expected


@pytest.mark.parametrize("phone, expected", [
    ("9876543210", True),
    ("1234567890", False),
    ("987654321", False),
])
def test_validate_phone(phone, expected):
    result = validate_phone(phone)
    assert (result is not None) == expected


@pytest.mark.parametrize("email, expected", [
    ("john.doe@example.com", True),
    ("john.doe.com", False),
    ("johndoe@", False),
])
def test_validate_email(email, expected):
    result = validate_email(email)
    assert (result is not None) == expected


# Test AddressBook System
@pytest.fixture
def address_book_system():
    system = AddressBookSystem()
    system.add_address_book("Personal")
    return system


def test_add_contact(address_book_system):
    contact = Contact(first_name="John", last_name="Doe", address="123 Main St", city="Hyderabad", state="Telangana",
                      zip_code="500001", phone_number="9876543210", email="john.doe@example.com")
    book = address_book_system.get_address_book("Personal")
    book.add_contact(contact)
    assert len(book.contacts) == 1


def test_edit_contact(address_book_system):
    old_contact = Contact(first_name="John", last_name="Doe", address="123 Main St", city="Hyderabad",
                          state="Telangana",
                          zip_code="500001", phone_number="9876543210", email="john.doe@example.com")
    new_contact = Contact(first_name="John", last_name="Smith", address="456 Main St", city="Hyderabad",
                          state="Telangana",
                          zip_code="500002", phone_number="9876543211", email="john.smith@example.com")

    book = address_book_system.get_address_book("Personal")
    book.add_contact(old_contact)

    assert book.edit_contact("John", new_contact) is True
    assert book.contacts[0].first_name == "John"
    assert book.contacts[0].last_name == "Smith"


def test_delete_contact(address_book_system):
    contact = Contact(first_name="John", last_name="Doe", address="123 Main St", city="Hyderabad", state="Telangana",
                      zip_code="500001", phone_number="9876543210", email="john.doe@example.com")
    book = address_book_system.get_address_book("Personal")
    book.add_contact(contact)

    assert book.delete_contact("John") is True
    assert len(book.contacts) == 0


def test_view_contacts_by_city_or_state(address_book_system):
    contact_1 = Contact(first_name="John", last_name="Doe", address="123 Main St", city="Hyderabad", state="Telangana",
                        zip_code="500001", phone_number="9876543210", email="john.doe@example.com")
    contact_2 = Contact(first_name="Jane", last_name="Doe", address="456 Main St", city="Bangalore", state="Karnataka",
                        zip_code="500002", phone_number="9876543211", email="jane.doe@example.com")

    book = address_book_system.get_address_book("Personal")
    book.add_contact(contact_1)
    book.add_contact(contact_2)

    result = address_book_system.search_person_contact_by_city_or_state(city="Hyderabad")
    assert len(result) == 1
    assert result[0].first_name == "John"

    result_state = address_book_system.search_person_contact_by_city_or_state(state="Karnataka")
    assert len(result_state) == 1
    assert result_state[0].first_name == "Jane"


def test_sort_contacts_by_name(address_book_system):
    contact_1 = Contact(first_name="John", last_name="Doe", address="123 Main St", city="Hyderabad", state="Telangana",
                        zip_code="500001", phone_number="9876543210", email="john.doe@example.com")
    contact_2 = Contact(first_name="Jane", last_name="Doe", address="456 Main St", city="Bangalore", state="Karnataka",
                        zip_code="500002", phone_number="9876543211", email="jane.doe@example.com")

    book = address_book_system.get_address_book("Personal")
    book.add_contact(contact_1)
    book.add_contact(contact_2)

    sorted_contacts = address_book_system.sort_contacts_by_name("Personal")
    assert sorted_contacts[0].first_name == "Jane"
    assert sorted_contacts[1].first_name == "John"


if __name__ == "__main__":
    pytest.main()
