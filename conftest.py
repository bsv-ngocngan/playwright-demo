import pytest
from pages.login_page import LoginPage
from pages.register_page import RegisterPage

@pytest.fixture
def access_to_login_page(page):
    login_page = LoginPage(page)
    login_page.navigate("https://playwright-demo.eventos.work/web/portal/529/event/3988/users/login")
    return login_page


@pytest.fixture
def access_to_register_page(page):
    register_page = RegisterPage(page)
    register_page.navigate("https://admin.odakyu.bravesoft.vn/account-management")
    register_page.page.get_by_role("button", name="新規追加").click()
    register_page.page.locator("#account_name").wait_for(state="visible")
    return register_page
