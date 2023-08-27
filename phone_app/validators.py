import phonenumbers


def format_phone_number_to_e164(phone):
    try:
        parsed_number = phonenumbers.parse(phone, None)
        if phonenumbers.is_valid_number(parsed_number):
            return phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.E164)
        else:
            return None
    except phonenumbers.NumberParseException:
        return None