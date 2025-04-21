from file_io import write_to_file, read_from_file
from Address_book import AddressBook
from schema import Contact

class AddressBookSystem:
    def __init__(self):
        self.address_books = {}

    def add_address_book(self, name: str):
        if name not in self.address_books:
            self.address_books[name] = AddressBook(name)

    def get_address_book(self, name: str):
        return self.address_books.get(name)

    def is_duplicate(self, book_name: str, first_name: str) -> bool:
        book = self.address_books.get(book_name)
        if book:
            return any(contact.first_name == first_name for contact in book.contacts)
        return False

    def search_person_contact_by_city_or_state(self, city=None, state=None):
        result = []
        for book in self.address_books.values():
            for contact in book.contacts:
                if (city and contact.city == city) or (state and contact.state == state):
                    result.append(contact)
        return result

    def view_by_city_or_state(self):
        city_dict = {}
        state_dict = {}
        for book in self.address_books.values():
            for contact in book.contacts:
                city_dict.setdefault(contact.city, []).append(contact)
                state_dict.setdefault(contact.state, []).append(contact)
        return city_dict, state_dict

    def count_by_city_or_state(self):
        city_dict, state_dict = self.view_by_city_or_state()
        return {city: len(people) for city, people in city_dict.items()}, \
               {state: len(people) for state, people in state_dict.items()}

    def sort_contacts_by_name(self, book_name: str):
        book = self.address_books.get(book_name)
        if book:
            return sorted(book.contacts, key=lambda c: (c.first_name, c.last_name))
        return []

    def sort_contacts_by_attribute(self, book_name: str, attribute: str):
        book = self.address_books.get(book_name)
        if book and hasattr(Contact, attribute):
            return sorted(book.contacts, key=lambda c: getattr(c, attribute))
        return []

    # Write address books to a file using the imported write_to_file function
    def write_to_file(self, filename: str):
        write_to_file(self.address_books, filename)

    # Read address books from a file using the imported read_from_file function
    def read_from_file(self, filename: str):
        self.address_books = read_from_file(filename)
