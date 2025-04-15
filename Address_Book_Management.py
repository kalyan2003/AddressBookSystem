
class Contact:
    def __init__(self,first_name,last_name,address,city,state,zip_code,phone_number,email):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.phone_number = phone_number
        self.email = email

    def __str__(self):
        return  f"{self.first_name} {self.last_name}, {self.address}, {self.city}, {self.state}, {self.zip_code}, {self.phone_number}, {self.email}"



class AddressBook:
    def __init__(self, name):
        self.name = name
        self.contacts = []

    def add_contact(self,contact):
        self.contacts.append(contact)


    def edit_contact(self,first_name,updated_contact):
        for i, contact in enumerate(self.contacts):
            if contact.first_name == first_name:
                self.contacts[i] == updated_contact
                return True

        return False

    def delete_contact(self,first_name):
        for contact in self.contacts:
            if contact.first_name == first_name:
                self.contacts.remove(contact)
                return True
        return False


class AddressBookSystem:
    def __init__(self):
        self.address_books = []

    def add_address_book(self,name):
        if name not in self.address_books:
            self.address_books[name] = AddressBook(name)


    def get_address_book(self,name):
        return self.address_books.get(name)


    def is_duplicate(self,book_name, first_name):
        book = self.address_books.get(book_name)
        if book:
            return any(contact.first_name == first_name for contact in book.contacts)
        return False


    def search_person_contact_by_city_or_state(self,city=None,state=None):
        result = []
        for book in self.address_books.values():
            for contact in book.contacts:
                if(city and contact.city == city) or (state and contact.state == state):
                    result.append(contact)
        return result


    def view_by_city_or_state(self):
        city_dict = {}
        state_dict = {}
        for book in self.address_books.values():
            for contact in book.contacts:
                city_dict.setdefult(contact.city,[]).append(contact)
                state_dict.setdefault(contact.state,[]).append(contact)
        return city_dict,state_dict

    def count_by_city_or_state(self):
        city_dict,state_dict = self.view_by_city_or_state()
        return {city: len(people) for city,people in city_dict.items()},{state: len(people) for state,people in state_dict.items()}

    def sort_contacts_by_name(self, book_name):
        book = self.address_books.get(book_name)
        if book:
            return sorted(book.contacts, key=lambda c: (c.first_name,c.last_name))
        return []

    def sort_contacts_by_attribute(self,book_name,attribute):
        book = self.address_books.get(book_name)
        if book and hasattr(Contact, attribute):
            return sorted(book.contacts,key=lambda c: getattr(c, attribute))
        return []



