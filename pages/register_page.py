from pages.base_page import BasePage

class RegisterPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.account_name = "//input[@id='account_name']"
        self.email_address = "//input[@id='mail_address']"
        self.password_input = "//input[@id='password']"
        self.role_switch = "//select[@id='role']"
        self.status_switch = "//select[@id='status']"   
        self.register_button = "//button[@id='register_button']" 

    def input_account_name(self, account_name): #hàm nhập account name
        self.fill(self.account_name, account_name)

    def input_email(self, email): #hàm nhập email
        self.fill(self.email_address, email)    

    def input_password(self, password): #hàm nhập password
        self.fill(self.password_input, password)
    
    def select_role(self, role): #hàm chọn role từ dropdown
        self.select_option(self.role_switch, role)

    def select_status(self, status): #hàm chọn status từ dropdown
        self.select_option(self.status_switch, status)

    def click_register(self): #hàm click register button
        self.click(self.register_button)        

    def goto_register_page(self): #hàm điều hướng đến trang đăng ký
        self.navigate("https://admin.odakyu.bravesoft.vn/account-management") 