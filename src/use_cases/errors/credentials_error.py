class CredentialsException(Exception):
    def __init__(self) -> None:
        super().__init__('Credentials are invalid')
        