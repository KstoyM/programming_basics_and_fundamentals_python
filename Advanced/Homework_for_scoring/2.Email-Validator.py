class NameTooShortError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


class MustContainAtSymbolError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


class InvalidDomainError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


while True:
    email = input()

    if email == 'End':
        break

    if '@' not in email:
        raise MustContainAtSymbolError("Email must contain @")

    symbol_index = email.find('@')
    name = email[:symbol_index]

    if len(name) <= 4:
        raise NameTooShortError("Name must be more than 4 characters")

    dot_index = email.find('.')
    domain = email[dot_index:]

    if domain not in ('.com', '.bg', '.net', '.org'):
        raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")

    print("Email is valid")
