
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
    

