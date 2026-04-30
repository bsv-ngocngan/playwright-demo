import pytest
import re
import os
from playwright.sync_api import expect, Error as PlaywrightError
from pages.register_page import RegisterPage

BASE_URL = "https://admin.odakyu.bravesoft.vn/login"
EMAIL = "kimtran@bravesoft.com.vn"
PASSWORD = "brave0404"


def debug_delay(page, ms=2000):
    if os.getenv("SLOW_MO") == "1":
        page.wait_for_timeout(ms)


def open_screen(page):
    page.goto(BASE_URL, wait_until="domcontentloaded", timeout=60000)

    email = page.locator("input#mail_address, input[name='email']").first
    password = page.locator("input#password, input[name='password']").first

    expect(email).to_be_visible(timeout=15000)
    email.fill(EMAIL)
    password.fill(PASSWORD)

    login_btn = page.get_by_role("button", name="ログイン")
    expect(login_btn).to_be_visible(timeout=10000)
    login_btn.click()
    debug_delay(page, 3000)

    expect(page).to_have_url(
        re.compile(r"^https://admin\.odakyu\.bravesoft\.vn/account-management/?$"),
        timeout=30000,
    )

    page.wait_for_load_state("domcontentloaded")

    new_btn = page.locator("button.common-submit-btn.primary:has-text('新規追加')").first
    expect(new_btn).to_be_visible(timeout=20000)
    expect(new_btn).to_be_enabled(timeout=20000)
    new_btn.scroll_into_view_if_needed()
    new_btn.click(timeout=10000)
    debug_delay(page, 5000)

    # Fallback click if first click is swallowed by overlay/state transition.
    popup = page.locator("div.modify-account-modal-content")
    try:
        expect(popup).to_be_visible(timeout=5000)
    except Exception:
        new_btn.click(force=True, timeout=10000)
        debug_delay(page, 5000)
    if os.getenv("DEBUG_POPUP") == "1":
        page.pause()
        expect(popup).to_be_visible(timeout=15000)

    # Assert title specifically inside the opened modal to avoid false positives.
    expect(popup.locator("div.title-confirm")).to_have_text("新規アカウント追加", timeout=10000)
    if os.getenv("DEBUG_SCREENSHOT") == "1":
        page.screenshot(path="popup_opened_debug.png", full_page=True)


@pytest.fixture(autouse=True)
def setup_each_test(page):
    open_screen(page)


@pytest.fixture
def access_to_register_page(page):
    return RegisterPage(page)


@pytest.fixture(autouse=True)
def pause_10s_each_test(page):
    yield
    if os.getenv("PAUSE_EACH_TEST", "0") != "1":
        return
    try:
        if not page.is_closed():
            page.wait_for_timeout(10000)
    except PlaywrightError:
        # Ignore teardown delay when page/context was already closed by browser/runtime.
        pass