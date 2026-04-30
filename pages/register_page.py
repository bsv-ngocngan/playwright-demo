from playwright.sync_api import Error as PlaywrightError
from playwright.sync_api import TimeoutError as PlaywrightTimeoutError

from pages.base_page import BasePage


class RegisterPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.page = page

        self.modal = page.get_by_role("dialog").filter(has_text="新規アカウント追加").first
        self.popup_title = self.modal.get_by_text("新規アカウント追加", exact=True)
        self.account_label = self.modal.get_by_text("アカウント名", exact=False).first
        self.email_label = self.modal.get_by_text("メールアドレス", exact=False).first
        self.password_label = self.modal.get_by_text("パスワード", exact=False).first
        self.role_label = self.modal.get_by_text("権限", exact=False).first
        self.status_label = self.modal.get_by_text("ステータス", exact=False).first
        self.switch_label = self.modal.get_by_text("チケット組成時のポイント付与パラメータの変更権限", exact=False).first
        self.switch_label_1 = self.modal.get_by_text("有", exact=False).first
        self.switch_label_2 = self.modal.get_by_text("無", exact=False).first

        self.email_input = self._input_after_label("メールアドレス")
        self.password_input = self._input_after_label("パスワード")
        self.role_input = (
            self.modal.get_by_role("combobox", name="権限").first.or_(
                self._select_after_label("権限")
            ).or_(
                self.modal.locator("div.label-title", has_text="権限").locator(
                    "xpath=following::*[(self::button) or (@role='combobox')][1]"
                ).first
            ).first
        )
        self.status_input = (
            self.modal.get_by_role("combobox", name="ステータス").first.or_(
                self._select_after_label("ステータス")
            ).first
        )
        self.save_button = self.modal.get_by_role("button", name="保存")
        self.cancel_button = self.modal.get_by_role("button", name="キャンセル")

    def _input_after_label(self, label_text):
        return self.modal.locator("div.label-title", has_text=label_text).locator(
            "xpath=following::input[1]"
        ).first

    def _select_after_label(self, label_text):
        return self.modal.locator("div.label-title", has_text=label_text).locator(
            "xpath=following::select[1]"
        ).first

    def get_popup_title(self):
        return self.popup_title
    
    def get_account_label(self):
        return self.account_label
    
    def get_email_label(self):
        return self.email_label
    
    def get_password_label(self):
        return self.password_label
    
    def get_role_label(self):
        return self.role_label
    
    def get_status_label(self):
        return self.status_label

    def get_password_placeholder(self):
        # Return locator so tests can assert visibility/attributes directly.
        return self.password_input

    def get_password_type(self):
        return self.password_input.get_attribute("type") == "password"

    def get_role_selectbox(self):
        return self.role_input

    def get_pulldownn_icon(self):
        return self.role_input.locator("xpath=following::*[self::i or self::svg][1]") 
    
    def get_role_selectbox_value(self):
        try:
            return self.role_input.input_value()
        except PlaywrightError:
            return (self.role_input.text_content() or "").strip()

    def _account_name_locator(self): 
        """User-facing account field based on nearby label."""
        return self._input_after_label("アカウント名")

    @property 
    def account_name_input(self):
        return self._account_name_locator()

    def input_account_name(self, account_name):
        inp = self.account_name_input
        inp.wait_for(state="visible", timeout=15000)
        inp.scroll_into_view_if_needed()
        try:
            inp.click(timeout=5000)
        except (PlaywrightTimeoutError, PlaywrightError):
            inp.click(timeout=5000, force=True)
        try:
            inp.fill(account_name, timeout=10000)
        except (PlaywrightTimeoutError, PlaywrightError):
            inp.fill(account_name, timeout=10000, force=True)
    
    def input_email(self, email):
        self.email_input.fill(email)
    
    def input_password(self, password):
        self.password_input.fill(password)
    
    def select_role(self, role):
        try:
            self.role_input.select_option(role)
            return
        except PlaywrightError:
            # Custom dropdown fallback: click trigger then select option by visible text.
            self.role_input.click()
            option = self.modal.get_by_role("option", name=role).first
            try:
                option.wait_for(state="visible", timeout=5000)
                option.click()
                return
            except PlaywrightTimeoutError:
                pass
            self.modal.get_by_text(role, exact=True).first.click()
    
    def set_status(self, status):
        self.status_input.select_option(status)

    def get_switch_label(self): 
        return self.modal.get_by_text("チケット組成時のポイント付与パラメータの変更権限", exact=True).first
    
    def get_switch_label_value(self): #value của switch_label
        return (self.get_switch_label().text_content() or "").strip()
    
    def get_switch_label_1(self):
        # Option "有"
        return self.get_switch_label().locator("xpath=following::label[contains(., '有')][1]").first
    
    def get_switch_label_2(self):
        # Option "無"
        return self.get_switch_label().locator("xpath=following::label[contains(., '無')][1]").first
    
    def switch_label_1_click(self):
        self.get_switch_label_1().click()
    
    def switch_label_2_click(self):
        self.get_switch_label_2().click()  

    def click_save_button(self):
        self.save_button.click()
    
    def register(self, account_name, email, password, role, status):
        self.input_account_name(account_name)
        self.input_email(email)
        self.input_password(password)
        self.select_role(role)
        self.set_status(status)
        self.click_save_button()
    
    def cancel_registration(self):
        self.cancel_button.click()
