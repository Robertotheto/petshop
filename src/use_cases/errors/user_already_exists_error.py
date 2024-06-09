class UserAlreadyExistsException(Exception):
    def __init__(self, email) -> None:
        self.email = email
        super().__init__(f'User with email {email} already exists')
    