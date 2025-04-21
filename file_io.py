import csv
from Address_book import AddressBook
from schema import Contact

# Write address books to a CSV file
def write_to_file(address_books, filename: str):
    for book_name, book in address_books.items():
        with open(f"{book_name}_{filename}", 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["First Name", "Last Name", "Address", "City", "State", "Zip Code", "Phone", "Email"])
            for contact in book.contacts:
                writer.writerow([contact.first_name, contact.last_name, contact.address, contact.city, contact.state,
                                 contact.zip_code, contact.phone_number, contact.email])

# Read address books from a CSV file
def read_from_file(filename: str):
    address_books = {}
    try:
        import os
        for file_name in os.listdir():
            if file_name.endswith(f"_{filename}"):
                book_name = file_name.split('_')[0]
                address_books[book_name] = AddressBook(book_name)

                with open(file_name, 'r') as file:
                    reader = csv.reader(file)
                    next(reader)  # Skip the header row
                    for row in reader:
                        contact = Contact(
                            first_name=row[0],
                            last_name=row[1],
                            address=row[2],
                            city=row[3],
                            state=row[4],
                            zip_code=row[5],
                            phone_number=row[6],
                            email=row[7]
                        )
                        address_books[book_name].add_contact(contact)
    except FileNotFoundError:
        print(f"The file {filename} does not exist.")
    except Exception as e:
        print(f"Error reading the file: {e}")
    return address_books
