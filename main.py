from Address_Book_Management import AddressBookSystem
from schema import get_contact_input

def print_welcome_msg():
    print("Welcome to Address Book System")

def main():
    print_welcome_msg()
    system = AddressBookSystem()
    filename = "address_book_data.json"
    system.read_from_file(filename)

    while True:
        print("\n1. Add Address Book")
        print("2. Add Contact")
        print("3. Edit Contact")
        print("4. Delete Contact")
        print("5. View All Contacts")
        print("6. Save and Exit")
        print("7. Exit Without Saving")

        choice = input("Choose an option: ")

        if choice == "1":
            name = input("Enter Address Book Name: ")
            system.add_address_book(name)

        elif choice == "2":
            book_name = input("Enter Address Book Name: ")
            book = system.get_address_book(book_name)
            if not book:
                print("Address Book not found.")
                continue

            contact = get_contact_input()
            if contact:
                if system.is_duplicate(book_name, contact.first_name):
                    print("Duplicate entry found!")
                else:
                    book.add_contact(contact)
                    print("Contact added.")

        elif choice == "3":
            book_name = input("Enter Address Book Name: ")
            first_name = input("Enter First Name to Edit: ")
            updated_contact = get_contact_input()
            if updated_contact:
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
                for contact in address_book.contacts:
                    print(contact)
            else:
                print("Address Book not found.")

        elif choice == "6":
            system.write_to_file(filename)  # Save the data before exiting
            print("Data saved. Exiting...")
            break

        elif choice == "7":
            print("Exiting without saving...")
            break

        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
