def test_register_001(access_to_register_page):
    """Verify register popup has browser title."""
    register_page = access_to_register_page

    assert register_page.page.title().strip() != ""

def test_register_002(access_to_register_page):
    """Display /account-management in URL"""
    register_page = access_to_register_page
    assert "/account-management" in register_page.page.url

#account name field
def test_register_003(access_to_register_page):
    """Display label アカウント名 * （255文字以内）"""
    register_page = access_to_register_page
    account_name_label = register_page.page.locator(
        "div.label-title", has_text="アカウント名"
    ).first
    assert account_name_label.is_visible()
    assert account_name_label.locator(".required-mark").text_content().strip() == "*"
    assert "255文字以内" in account_name_label.locator(".input-note").text_content()

def test_register_004(access_to_register_page):
    """Display when input account name"""
    register_page = access_to_register_page
    register_page.input_account_name("ngocngan")
    assert register_page.get_input_value(register_page.account_name) == "ngocngan"

