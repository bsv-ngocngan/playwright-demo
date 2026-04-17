from pages.base_page import BasePage
from pages.login_page import LoginPage


#check field email 005 - 014
    def test_login_005(access_to_login_page):
        """Check if field [email] is displayed label and textbox on the login page."""
        login_page = access_to_login_page

        assert login_page.is_text_visible("メールアドレス")
        assert login_page.is_element_visible(login_page.email_input)

    def test_login_006(access_to_login_page):
        """Check if user can input text into username and password fields."""
        login_page = access_to_login_page
        login_page.input_email("NNNngocngan")
        login_page.input_password("zzzz")

        assert login_page.get_input_value(login_page.email_input) == "NNNngocngan"
        assert login_page.get_input_value(login_page.password_input) == "zzzz"

    def test_login_007(access_to_login_page):
        """Check data display in field [email]."""
        login_page = access_to_login_page
        login_page.input_email("abc@gmail.com")

        assert login_page.get_input_value(login_page.email_input) == "abc@gmail.com"

    def test_login_008(access_to_login_page):
        """Check data display in field [email]."""
        login_page = access_to_login_page
        login_page.input_email("ABC@GMAIL.COM")

        assert login_page.get_input_value(login_page.email_input) == "ABC@GMAIL.COM"

    def test_login_009(access_to_login_page):
        """Check error message if invalid data is entered in field [email]."""
        login_page = access_to_login_page
        login_page.input_email("abc@gmail")

        assert login_page.is_text_visible("メールアドレスが正しくありません。")

    def test_login_010(access_to_login_page):
        """Check error message if invalid data is entered in field [email]."""
        login_page = access_to_login_page
        login_page.input_email("abc!@gmail.com")

        assert login_page.is_text_visible("メールアドレスが正しくありません。")

    def test_login_011(access_to_login_page):
        """Check error message if invalid data is entered in field [email]."""
        login_page = access_to_login_page
        login_page.input_email("test.abc")

        assert login_page.is_text_visible("メールアドレスが正しくありません。")

    def test_login_012(access_to_login_page):
        """Check error message if invalid data is entered in field [email]."""
        login_page = access_to_login_page
        login_page.input_email("@gmail.com")
        login_page.input_password("123456")
        login_page.click_login()
        assert login_page.is_text_visible("メールアドレスが正しくありません。")

    def test_login_013(access_to_login_page): 
        """Check error message if full-width character is entered in field [email]."""
        login_page = access_to_login_page
        login_page.input_email("あああああ")

        assert login_page.is_text_visible("メールアドレスが正しくありません 。" )

    def test_login_014(access_to_login_page):
        """Check error message if inputed data is cleard from field [email]."""
        login_page = access_to_login_page
        login_page.input_email("テスト@テスト.テスト")
        login_page.clear_input(login_page.email_input)

        assert login_page.is_text_visible("メールアドレスが正しくありません 。" )


#check field [password] 015 - 026
    def test_login_015(access_to_login_page):
        """Check if field [password] is displayed label and textbox on the login page."""
        login_page = access_to_login_page

        assert login_page.is_text_visible("パスワード")
        assert login_page.is_element_visible(login_page.password_input) 