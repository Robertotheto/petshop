class UserCredentialsException(Exception):
    def __init__(self) -> None:
        super().__init__('User credentials are invalid')
        