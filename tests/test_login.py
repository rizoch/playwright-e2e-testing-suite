import pytest
from pages.login_page import LoginPage

def login_sequence(page, user, password):
    login = LoginPage(page)
    login.load()
    login.login(user, password)
    return login

@pytest.mark.parametrize(
    "username,password,expected_url,expected_type",
    [
        ("standard_user", "secret_sauce", "inventory", None),
        ("locked_out_user", "secret_sauce", None, "locked out"),
        ("", "secret_sauce", None,"username is required"),
        ("standard_user", "", None,"password is required"),
        ("standard_user", "stalkwowal", None,"do not match"),
        ("s", "secret_sauce", None, "do not match")
    ]
)
def test_login_cases(page, username, password, expected_url, expected_type):
    login = login_sequence(page, username, password)
    if expected_url:
        assert expected_url in page.url
    if expected_type:
        assert expected_type in login.get_error().lower()