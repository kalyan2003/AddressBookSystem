import json
from Address_book import AddressBook
from schema import Contact

# Write address books to a file
def write_to_file(address_books, filename: str):
    with open(filename, 'w') as file:
        data = {book_name: [contact.dict() for contact in book.contacts] for book_name, book in address_books.items()}
        json.dump(data, file, indent=4)

# Read address books from a file
def read_from_file(filename: str):
    address_books = {}
    try:
        with open(filename, 'r') as file:
            data = json.load(file)
            for book_name, contacts in data.items():
                address_books[book_name] = AddressBook(book_name)
                for contact_data in contacts:
                    contact = Contact(**contact_data)
                    address_books[book_name].add_contact(contact)
    except FileNotFoundError:
        print(f"The file {filename} does not exist.")
    except json.JSONDecodeError:
        print("Error reading the file. It may be corrupted or improperly formatted.")
    return address_books
