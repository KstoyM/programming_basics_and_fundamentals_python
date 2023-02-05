from re import findall


class NameTooShortError(Exception):
    pass


class MustContainAtSymbolError(Exception):
    pass


class InvalidDomainError(Exception):
    pass


class MoreThanOneAtSymbolsError(Exception):
    pass


class InvalidNameError(Exception):
    pass


name_pattern = r'[\w+\.]+'
domain_pattern = r'\.[a-z]+'

valid_domains = ['.com', ".bg", ".net", ".org"]
email = input()

while email != 'End':

    try:
        if email.count('@') > 1:
            raise MoreThanOneAtSymbolsError("Email should contain only one @!")
        if len(email.split("@")[0]) <= 4:
            raise NameTooShortError("Name must be more than 4 characters")
        if findall(name_pattern, email)[0] != email.split("@")[0]:
            raise InvalidNameError("Name can only contain numbers, letters, underscores and dots.")
        if "@" not in email:
            raise MustContainAtSymbolError("Email must contain @")
        if findall(domain_pattern, email)[-1] not in valid_domains:
            raise InvalidDomainError(f"Domain must be one of the following: {', '.join(valid_domains)}")

    except IndexError:
        print("Invalid email")

    else:
        print("Email is valid")
        
    email = input()
