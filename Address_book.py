from schema import Contact

class AddressBook:
    def __init__(self, name):
        self.name = name
        self.contacts = []

    def add_contact(self, contact: Contact):
        self.contacts.append(contact)

    def edit_contact(self, first_name: str, updated_contact: Contact) -> bool:
        for i, contact in enumerate(self.contacts):
            if contact.first_name == first_name:
                self.contacts[i] = updated_contact
                return True
        return False

    def delete_contact(self, first_name: str) -> bool:
        for contact in self.contacts:
            if contact.first_name == first_name:
                self.contacts.remove(contact)
                return True
        return False
