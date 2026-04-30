def test_1_title(access_to_register_page):
    """popup title"""
    register_page = access_to_register_page
    modal_title = register_page.popup_title
    assert modal_title.is_visible()
    assert modal_title.text_content().strip() == "新規アカウント追加"

def test_2_url(access_to_register_page):
    """Verify url page inside register popup."""
    register_page = access_to_register_page
    assert register_page.page.url == "https://admin.odakyu.bravesoft.vn/account-management"

def test_3_account_label(access_to_register_page):
    """account label"""
    register_page = access_to_register_page
    account_label = register_page.get_account_label()
    assert account_label.is_visible()
    assert account_label.locator(".required-mark").text_content().strip() == "*"
    assert "255文字以内" in (account_label.locator(".input-note").text_content() or "")

def test_4_input_account(access_to_register_page):
    """input account name"""
    register_page = access_to_register_page
    register_page.input_account_name("ngocngan")
    assert register_page.account_name_input.is_visible()
    assert register_page.account_name_input.input_value() == "ngocngan"


def test_5_email_label(access_to_register_page):
    """email label"""
    register_page = access_to_register_page
    email_label = register_page.get_email_label()
    assert email_label.is_visible()
    assert "メールアドレス" in (email_label.text_content() or "")

def test_6_input_email(access_to_register_page):
    """input valid email"""
    register_page = access_to_register_page
    register_page.input_email("trucly@bravesoft-vn.com.vn")
    assert register_page.email_input.is_visible()
    assert register_page.email_input.input_value() == "trucly@bravesoft-vn.com.vn"

def test_7_password_label(access_to_register_page): #「パスワード」（半角英数字  8文字以上32文字以内）ラベルが表示されること
    """password label"""
    register_page = access_to_register_page
    password_label = register_page.get_password_label()
    assert password_label.is_visible()
    assert password_label.text_content().strip() == "パスワード（半角英数字  8文字以上32文字以内）"

def test_8_password_placeholder(access_to_register_page):
    """password placeholders should be masked"""
    register_page = access_to_register_page
    password_placeholder = register_page.get_password_placeholder()
    assert password_placeholder.is_visible()
    assert password_placeholder.get_attribute("type") == "password"

def test_9_input_password(access_to_register_page):
    """input password should be masked"""
    register_page = access_to_register_page
    register_page.input_password("NNqv12345678")
    assert register_page.password_input.is_visible()
    assert register_page.password_input.input_value() == "NNqv12345678"
    assert register_page.password_input.get_attribute("type") == "password"

def test_10_role_selectbox(access_to_register_page):
    """select box should be blank by default"""
    register_page = access_to_register_page
    role_selectbox = register_page.get_role_selectbox()
    assert role_selectbox.is_visible()
    assert register_page.get_role_selectbox_value() in ""

def test_11_select_role(access_to_register_page):
    """select role マスター管理者"""
    register_page = access_to_register_page
    register_page.select_role("マスター管理者")
    role_text = register_page.get_role_selectbox_value()
    assert role_text == "マスター管理者"

def test_12_select_role(access_to_register_page):
    """select role テナント管理者"""
    register_page = access_to_register_page
    register_page.select_role("テナント管理者")
    role_text = register_page.get_role_selectbox_value()
    assert "テナント管理者" in role_text

def test_13_select_role(access_to_register_page):
    """select both role マスター管理者 and テナント管理者""" #同時に「マスター管理者」と「テナント管理者」を選択する
    register_page = access_to_register_page
    register_page.select_role("マスター管理者")
    register_page.select_role("テナント管理者")
    role_text = register_page.get_role_selectbox_value()
    assert role_text == "テナント管理者"

def test_14_select_role(access_to_register_page): #case này hong trả kết quả Nhun ơi
    """status label"""
    register_page = access_to_register_page
    register_page.select_role("テナント管理者")
    switch_label = register_page.get_switch_label()
    switch_label.wait_for(state="visible", timeout=10000)
    assert "ポイント付与パラメータ" in register_page.get_switch_label_value()
    assert register_page.get_switch_label_1().is_visible()
    assert register_page.get_switch_label_2().is_visible()
    assert register_page.get_switch_label_1().text_content().strip() == "有"
    assert register_page.get_switch_label_2().text_content().strip() == "無"

def test_15_switch_label_1_click(access_to_register_page):
    """switch label 1 click"""
    register_page = access_to_register_page
    register_page.select_role("テナント管理者")
    switch_label = register_page.get_switch_label()
    switch_label.wait_for(state="visible", timeout=10000)
    register_page.switch_label_1_click()
    assert "有" in register_page.get_switch_label_value()

def test_16_switch_label_2_click(access_to_register_page):
    """switch label 2 click"""
    register_page = access_to_register_page
    register_page.select_role("テナント管理者")
    switch_label = register_page.get_switch_label()
    switch_label.wait_for(state="visible", timeout=10000)
    register_page.switch_label_2_click()
    assert "無" in register_page.get_switch_label_value()

#同時に「有」と「無」を選択する
def test_17_switch_label_1_and_2_click(access_to_register_page):
    """switch label 1 and 2 click"""
    register_page = access_to_register_page 
    register_page.select_role("テナント管理者")
    switch_label = register_page.get_switch_label()
    switch_label.wait_for(state="visible", timeout=10000)   
    register_page.switch_label_1_click()
    register_page.switch_label_2_click()
    assert "無" in register_page.get_switch_label_value()
