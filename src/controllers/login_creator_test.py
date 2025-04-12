import pytest

from src.drivers.password_handler import PasswordHandler

from .login_creator import LoginCreator

username = "meuUsername"
password = "minhaSenha"
hashed_password = PasswordHandler().encrypt_passwor(password)


class MockeUserRepository:
    def get_user_by_username(self, username):
        return (10, username, hashed_password)


def test_create():
    login_creator = LoginCreator(MockeUserRepository())
    response = login_creator.create(username, password)

    assert response["access"] is True
    assert response["username"] == username
    assert response["token"] is not None


def test_create_with_wrong_password():
    login_creator = LoginCreator(MockeUserRepository())

    with pytest.raises(Exception):
        login_creator.create(username, "algumaSenha")
