import pytest
from pages.login_page import LoginPage

@pytest.fixture
def access_to_login_page(page):
    login_page = LoginPage(page)
    login_page.navigate("https://playwright-demo.eventos.work/web/portal/529/event/3988/users/login")
    return login_page