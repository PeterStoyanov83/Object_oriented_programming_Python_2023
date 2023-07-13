class Profile:
    def __init__(self, username: str, password: str) -> None:
        self.username = self.validate_username(username)
        self.password = self.validate_password(password)

    def validate_username(self, username: str) -> str:
        if len(username) < 5 or len(username) > 15:
            raise ValueError("The username must be between 5 and 15 characters.")
        return username

    def validate_password(self, password: str) -> str:
        if (
                len(password) < 8
                or not any(char.isupper() for char in password)
                or not any(char.isdigit() for char in password)
        ):
            raise ValueError(
                "The password must be 8 or more characters with at least 1 digit and 1 uppercase letter."
            )
        return password

    def __str__(self):
        return f'You have a profile with username: "{self.username}" and password: {"*" * len(self.password)}'
