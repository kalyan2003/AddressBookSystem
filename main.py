import re


def Print_welcome_msg():
    print("Welcome to Address Book System")

def validate_first_and_last_name(name):
    pattern = r"^[A-Z][a-z]{2,}$"

    if re.match(pattern,name):
        return True
    else:
        return False

def validate_address(address):
    pattern = r"[A-Za-z0-9]{10,}$"

    if re.match(pattern,address):
        return True
    else:
        return False

def validate_city(city):
    pattern = r"^[A-Za-z]+$"

    if re.match(pattern,city):
        return True
    else:
        return False

def validate_zip_code(zip_code):
    pattern = r"^\d{6}$"

    if re.match(pattern,zip_code):
        return True
    else:
        return False

def validate_phone_number(phone):
    pattern = r"^[6-9][0-9]{9}$"
    if re.match(pattern,phone):
        return True
    else:
        return False

def validate_email_id(email):
    pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    if re.match(pattern,email):
        return True
    else:
        return False


if __name__ == "__main__":
    first_name = input("Enter your first name:")
    if validate_first_and_last_name(first_name):
        pass
    else:
        print("Enter the valid user name")

    last_name = input("Enter your last name:")
    if validate_first_and_last_name(last_name):
        pass
    else:
        print("Enter the valid last name")

    address = input("Enter your address:")
    if validate_address(address):
        pass
    else:
        print("Enter the valid address")

    city = input("Enter your city name :")
    if validate_city(city):
        pass
    else:
        print("Enter the valid city name")

    state = input("Enter the state name:")
    if validate_city(state):
        pass
    else:
        print("Enter the valid state name")

    zip_code = input("Enter your zip code:")
    if validate_zip_code(zip_code):
        pass
    else:
        print("Print the valid Zip code:")

    phone = input("Enter your mobile number :")
    if validate_phone_number(phone):
        pass
    else:
        print("Enter a valid mobile number :")

    email = input("Enter your email id :")
    if validate_email_id(email):
        pass
    else:
        print("Enter the valid Email id")



