import re
from functools import wraps

def validate_input(pattern, error_message):
    def decorator(func):
        @wraps(func)
        def wrapper(value):
            if re.match(pattern, value):
                return value
            else:
                print(error_message)
                return None
        return wrapper
    return decorator

# Validators for each field using the above generic decorator
@validate_input(r"^[A-Z][a-z]{2,}$", "Enter a valid first name (Capital + at least 3 letters)")
def validate_first_name(value: str): return value

@validate_input(r"^[A-Z][a-z]{2,}$", "Enter a valid last name (Capital + at least 3 letters)")
def validate_last_name(value: str): return value

@validate_input(r"[A-Za-z0-9\s]{10,}$", "Enter a valid address (min 10 characters)")
def validate_address(value: str): return value

@validate_input(r"^[A-Za-z\s]+$", "Enter a valid city name")
def validate_city(value: str): return value

@validate_input(r"^[A-Za-z\s]+$", "Enter a valid state name")
def validate_state(value: str): return value

@validate_input(r"^\d{6}$", "Enter a valid 6-digit zip code")
def validate_zip_code(value: str): return value

@validate_input(r"^[6-9][0-9]{9}$", "Enter a valid 10-digit mobile number starting with 6-9")
def validate_phone(value: str): return value

@validate_input(r"^[\w\.-]+@[\w\.-]+\.\w+$", "Enter a valid email address")
def validate_email(value: str): return value
