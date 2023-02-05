import re

email_input = input('Enter your email: ')
valid_domains = r'\b(bg|com|net|org)'


class NameTooShortError(Exception):
    pass


class MustContainAtSymbolError(Exception):
    pass


class InvalidDomainError(Exception):
    pass


while email_input != 'End':

    if len(email_input.split("@")[0]) < 4:
        raise NameTooShortError("Name must be more than 4 characters")

    if '@' not in email_input:
        raise MustContainAtSymbolError("Email must contain @")

    extension = email_input.split(".")[-1]
    is_extension_valid = re.match(valid_domains, email_input.split('.')[-1])

    if not is_extension_valid:
        raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")

    print("Email is valid")

    email_input = input('Enter your email: ')