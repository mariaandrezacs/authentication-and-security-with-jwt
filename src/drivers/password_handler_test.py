from .password_handler import PasswordHandler


def test_encrypt():
    minha_senha = "123RocketENois"
    password_handler = PasswordHandler()

    hashed_password = password_handler.encrypt_passwor(minha_senha)
    # print(hashed_password)
    password_checked = password_handler.check_password(minha_senha, hashed_password)
    # print(password_checked)

    assert password_checked
