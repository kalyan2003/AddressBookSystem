import re
from Address_Book_Management import Contact, AddressBookSystem

def Print_welcome_msg():
    print("Welcome to Address Book System")

def validate_first_and_last_name(name):
    pattern = r"^[A-Z][a-z]{2,}$"
    return bool(re.match(pattern, name))

def validate_address(address):
    pattern = r"[A-Za-z0-9\s]{10,}$"
    return bool(re.match(pattern, address))

def validate_city(city):
    pattern = r"^[A-Za-z\s]+$"
    return bool(re.match(pattern, city))

def validate_zip_code(zip_code):
    pattern = r"^\d{6}$"
    return bool(re.match(pattern, zip_code))

def validate_phone_number(phone):
    pattern = r"^[6-9][0-9]{9}$"
    return bool(re.match(pattern, phone))

def validate_email_id(email):
    pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    return bool(re.match(pattern, email))

def get_contact_input():
    while True:
        first_name = input("Enter your first name: ")
        if validate_first_and_last_name(first_name):
            break
        print("Enter a valid first name (Capital + at least 3 letters)")

    while True:
        last_name = input("Enter your last name: ")
        if validate_first_and_last_name(last_name):
            break
        print("Enter a valid last name (Capital + at least 3 letters)")

    while True:
        address = input("Enter your address: ")
        if validate_address(address):
            break
        print("Enter a valid address (min 10 characters)")

    while True:
        city = input("Enter your city: ")
        if validate_city(city):
            break
        print("Enter a valid city name")

    while True:
        state = input("Enter your state: ")
        if validate_city(state):
            break
        print("Enter a valid state name")

    while True:
        zip_code = input("Enter your zip code: ")
        if validate_zip_code(zip_code):
            break
        print("Enter a valid 6-digit zip code")

    while True:
        phone = input("Enter your mobile number: ")
        if validate_phone_number(phone):
            break
        print("Enter a valid 10-digit mobile number starting with 6-9")

    while True:
        email = input("Enter your email ID: ")
        if validate_email_id(email):
            break
        print("Enter a valid email address")

    return Contact(first_name, last_name, address, city, state, zip_code, phone, email)

def main():
    Print_welcome_msg()
    system = AddressBookSystem()

    while True:
        print("\n1. Add Address Book")
        print("2. Add Contact")
        print("3. Edit Contact")
        print("4. Delete Contact")
        print("5. View All Contacts")
        print("6. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            name = input("Enter Address Book Name: ")
            system.add_address_book(name)

        elif choice == "2":
            book_name = input("Enter Address Book Name: ")
            if not system.get_address_book(book_name):
                print("Address Book not found.")
                continue

            contact = get_contact_input()
            if system.is_duplicate(book_name, contact.first_name):
                print("Duplicate entry found!")
            else:
                system.get_address_book(book_name).add_contact(contact)
                print("Contact added.")

        elif choice == "3":
            book_name = input("Enter Address Book Name: ")
            first_name = input("Enter First Name to Edit: ")
            updated_contact = get_contact_input()
            if system.get_address_book(book_name).edit_contact(first_name, updated_contact):
                print("Contact updated.")
            else:
                print("Contact not found.")

        elif choice == "4":
            book_name = input("Enter Address Book Name: ")
            first_name = input("Enter First Name to Delete: ")
            if system.get_address_book(book_name).delete_contact(first_name):
                print("Contact deleted.")
            else:
                print("Contact not found.")

        elif choice == "5":
            book_name = input("Enter Address Book Name: ")
            address_book = system.get_address_book(book_name)
            if address_book:
                contacts = address_book.contacts
                for contact in contacts:
                    print(contact)
            else:
                print("Address Book not found.")

        elif choice == "6":
            print("Exiting...")
            break

        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
