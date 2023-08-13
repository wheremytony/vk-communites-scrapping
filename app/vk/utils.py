from re import (
    search,
)

PHONE_NUMBER_REGEX = r"(\+?\d?(\d{11})|(\d.\(?\d{3}\)?.\d{3}.\d{2}.\d{2}))"


def get_phone_number(text: str) -> str:
    match = search(PHONE_NUMBER_REGEX, text)
    phone_number = match[0]
    if len(phone_number) > 11:
        return "ПИЗДА"
    return "".join(filter(str.isdigit, match[0])) if match else "ПИЗДА"
