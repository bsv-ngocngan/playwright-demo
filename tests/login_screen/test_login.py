from pages import login_page
from pages.base_page import BasePage
from pages.login_page import LoginPage


#Verify field email 005 - 014
def test_login_005(access_to_login_page):
     """Verify email label and input display."""
     login_page = access_to_login_page
     assert login_page.is_text_visible("メールアドレス")
     assert login_page.is_element_visible(login_page.email_input)

def test_login_006(access_to_login_page):
    """Verify email input accept text """
    login_page = access_to_login_page
    login_page.input_email("NNNngocngan")
    assert login_page.get_input_value(login_page.email_input) == "NNNngocngan"

def test_login_007(access_to_login_page):
    """Display abc@gmail.com in email input"""
    login_page = access_to_login_page
    login_page.input_email("abc@gmail.com")
    assert login_page.get_input_value(login_page.email_input) == "abc@gmail.com"

def test_login_008(access_to_login_page):
    """Display ABC@GMAIL.COM in email input."""
    login_page = access_to_login_page
    login_page.input_email("ABC@GMAIL.COM")

    assert login_page.get_input_value(login_page.email_input) == "ABC@GMAIL.COM"

def test_login_009(access_to_login_page):
    """Show error message when input invalid email abc@gmail"""
    login_page = access_to_login_page
    login_page.input_email("abc@gmail")
    assert login_page.is_text_visible("メールアドレスが正しくありません。")

def test_login_010(access_to_login_page):
    """Show error message when input invalid email abc!@gmail.com"""
    login_page = access_to_login_page
    login_page.input_email("abc!@gmail.com")
    assert login_page.is_text_visible("メールアドレスが正しくありません。")

def test_login_011(access_to_login_page):
    """Show error message when input invalid email test.abc"""
    login_page = access_to_login_page
    login_page.input_email("test.abc")
    assert login_page.is_text_visible("メールアドレスが正しくありません。")

def test_login_012(access_to_login_page):
    """Show error message when input invalid email @gmail.com"""
    login_page = access_to_login_page
    login_page.input_email("@gmail.com")
    login_page.input_password("123456")
    login_page.click_login()
    assert login_page.is_text_visible("メールアドレスが正しくありません。")

def test_login_013(access_to_login_page): 
    """Show error message when input full-width character あああああ"""
    login_page = access_to_login_page
    login_page.input_email("あああああ")

    assert login_page.is_text_visible("メールアドレスが正しくありません 。" )

def test_login_014(access_to_login_page):
    """Show error message when input full-width character テスト@テスト.テスト"""
    login_page = access_to_login_page
    login_page.input_email("testabc@gmailcom")
    login_page.clear_input(login_page.email_input)
    assert login_page.is_text_visible("メールアドレスが正しくありません 。" )

#Verify field password 015 - 026
def test_login_015(access_to_login_page):
    """Verify password label, input and mask icon state."""
    login_page = access_to_login_page
    assert login_page.is_text_visible("パスワード") 
    assert login_page.is_element_visible(login_page.password_input) 
    assert login_page.is_element_visible(login_page.password_toggle_icon)

def test_login_016(access_to_login_page):
    """Password input should be masked"""
    login_page = access_to_login_page # lấy đối tượng login_page từ fixture access_to_login_page
    login_page.input_password("zzzz") #nhập password "zzzz" vào trường password
    #kiểm tra xem password có đang bị masked hay không bằng cách gọi hàm is_password_masked() và assert kết quả trả về là True nếu password đang bị masked
    assert login_page.is_password_masked()

def test_login_017(access_to_login_page):
    login_page = access_to_login_page
    login_page.input_password("zzzz")
    login_page.click(login_page.password_toggle_icon)
    assert login_page.is_password_unmasked()

def test_login_018_toggle_password_twice(access_to_login_page): 
    """Click eye icon twice to hide password.""" #reuse test case 016 and 017 để kiểm tra toggle password
    login_page = access_to_login_page
    login_page.input_password("zzzz")
    assert login_page.is_password_masked()
    #Click icon lần 1 → unmask password
    login_page.click(login_page.password_toggle_icon)
    assert login_page.is_password_unmasked()

    # Click icon lần 2 → mask lại
    login_page.click(login_page.password_toggle_icon)
    assert login_page.is_password_masked()

def test_login_019(access_to_login_page):
    """Show error message when input password less than minlength (8 characters)"""
    login_page = access_to_login_page
    login_page.input_password("asd12345")
    assert login_page.is_text_visible("「パスワードは8文字以上32文字以下で指定してください。」")

def test_login_020(access_to_login_page):   
    """Show error message when input password more than maxlength (32 characters)."""
    login_page = access_to_login_page
    login_page.input_password("a"*40)
    assert login_page.is_text_visible("「パスワードは8文字以上32文字以下で指定してください。」")

def test_login_021(access_to_login_page):
    """Verify no error message if password contains only numbers"""
    login_page = access_to_login_page
    login_page.input_password("1113331111212")
    assert login_page.is_password_masked()
    assert not login_page.is_text_visible("「パスワードは8文字以上32文字以下で指定してください。」")

def test_login_022(access_to_login_page):
    """Verify no error message if password contains UPPER+lower characters"""
    login_page = access_to_login_page
    login_page.input_password("AAbbPPooo")
    assert login_page.is_password_masked()
    assert not login_page.is_text_visible("「パスワードは8文字以上32文字以下で指定してください。」")

def test_login_023(access_to_login_page):
    """Verify no error message if password contains special characters"""
    login_page = access_to_login_page
    login_page.input_password("!@#$%^&*()_+")
    assert login_page.is_password_masked()
    assert not login_page.is_text_visible("「パスワードは8文字以上32文字以下で指定してください。」")

def test_login_024(access_to_login_page):   
    """Verify no error message if password contains mix of characters"""
    login_page = access_to_login_page
    login_page.input_password("Aa12345!@#")
    assert login_page.is_password_masked()
    assert not login_page.is_text_visible("「パスワードは8文字以上32文字以下で指定してください。」")

def test_login_025(access_to_login_page):
    """Input valid numeric and alphabet characters"""""
    login_page = access_to_login_page
    login_page.input_password("Aa12345")
    assert login_page.is_password_masked()
    assert not login_page.is_text_visible("「パスワードは8文字以上32文字以下で指定してください。」")

def test_login_026(access_to_login_page):
    """Input valid numberic and symbol characters"""
    login_page = access_to_login_page
    login_page.input_password("12345!@#")
    assert login_page.is_password_masked()
    assert not login_page.is_text_visible("「パスワードは8文字以上32文字以下で指定してください。」")    

#check forgot password link 027 - 028
def test_login_027(access_to_login_page):
    """Verify forgot password link"""
    login_page = access_to_login_page
    assert login_page.is_text_visible("パスワードを忘れた方はこちら")  

def test_login_028(access_to_login_page):
    """Navigate to forgot password link"""
    login_page = access_to_login_page
    login_page.click("text=パスワードを忘れた方はこちら")
    assert login_page.is_text_visible("パスワード再設定")

#check tính năng login 029 ~ 032
def test_login_029(access_to_login_page):
    """Default state of login button with empty email and password""" 
    login_page = access_to_login_page
    assert login_page.is_element_visible(login_page.login_button)
    assert login_page.is_element_disabled(login_page.login_button)

def test_login_030(access_to_login_page):
    """Not login with valid email and invalid password"""
    login_page = access_to_login_page
    login_page.input_email("kimtran@bravesoft.com.vn")
    login_page.input_password("invalid")
    login_page.click(login_page.login_button)
    assert login_page.is_text_visible("「ログインできませんでした。入力内容をご確認の上、もう一度お試しください。")

def test_login_031(access_to_login_page):
    """Not login with invalid email and valid password"""
    login_page = access_to_login_page
    login_page.input_email("invalid@example.com")
    login_page.input_password("brave0404")
    login_page.click(login_page.login_button)
    assert login_page.is_text_visible("「ログインできませんでした。入力内容をご確認の上、もう一度お試しください。")

def test_login_032(access_to_login_page):
    """Login successfully with valid email and password"""
    login_page = access_to_login_page
    login_page.input_email("kimtran@bravesoft.com.vn")  
    login_page.input_password("brave0404")
    login_page.click(login_page.login_button)
    assert login_page.is_text_visible("プロファイル")

#check button đăng ký
def test_login_033(access_to_login_page):
    """Verify register button display"""
    login_page = access_to_login_page
    assert login_page.is_text_visible("新規登録")

def test_login_034(access_to_login_page):
    """Navigate to register screen"""
    login_page = access_to_login_page
    login_page.click("text=新規登録")
    assert login_page.is_text_visible("新規登録")