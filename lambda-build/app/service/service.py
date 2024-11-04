from ..dependencies import User


def health_check():
    return True


def add_user(username: str, pretty_print: bool, body: User) -> None:
    return


def get_user_by_name(username: str) -> User:
    return User(username=username)
