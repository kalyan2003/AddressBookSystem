from pydantic import BaseModel
from validators_utils import (
    validate_first_name,
    validate_last_name,
    validate_address,
    validate_city,
    validate_state,
    validate_zip_code,
    validate_phone,
    validate_email
)
from typing import get_type_hints

class Contact(BaseModel):
    first_name: str
    last_name: str
    address: str
    city: str
    state: str
    zip_code: str
    phone_number: str
    email: str

def get_contact_input():

    field_names = get_type_hints(Contact).keys()
    input_data = {}

    for field in field_names:
        while True:
            value = input(f"{field.replace('_', ' ').title()}: ").strip()

            # Apply the corresponding validator function for each field
            if field == "first_name":
                validated_value = validate_first_name(value)
            elif field == "last_name":
                validated_value = validate_last_name(value)
            elif field == "address":
                validated_value = validate_address(value)
            elif field == "city":
                validated_value = validate_city(value)
            elif field == "state":
                validated_value = validate_state(value)
            elif field == "zip_code":
                validated_value = validate_zip_code(value)
            elif field == "phone_number":
                validated_value = validate_phone(value)
            elif field == "email":
                validated_value = validate_email(value)


            if validated_value:
                input_data[field] = validated_value
                break
            else:
                print(f"Invalid {field.replace('_', ' ')}. Please try again.")

    try:
        return Contact(**input_data)
    except Exception as e:
        print("Validation Error:", e)
        return None
