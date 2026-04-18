from pages.base_page import BasePage
class LoginPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.email_input = "//input[@id='mail_address']"
        self.password_input = "//input[@id='password']"
        self.login_button = "//button[@id='login_button']"
        self.password_toggle_icon = "//button[contains(@class,'password-toggle')]"      

    def input_email(self, email): #hàm nhập email
        self.fill(self.email_input, email)
    
    def input_password(self, password): #hàm nhập password
        self.fill(self.password_input, password)
    
    def click_login(self): #hàm click login button
        self.click(self.login_button)   
    
    def click_password_icon(self): #hàm click vào icon để toggle hiển thị password
        self.click(self.password_toggle_icon)

    def is_password_masked(self): #hàm kiểm tra xem password có bị ẩn hay không bằng cách kiểm tra thuộc tính "type" của input password
        return self.get_attribute(self.password_input, "type") == "password" #nếu thuộc tính "type" là "password" thì password đang được masked

    def is_password_unmasked(self): #hàm kiểm tra xem password có đang được hiển thị hay không bằng cách kiểm tra thuộc tính "type" của input password
        return self.get_attribute(self.password_input, "type") == "text" #nếu thuộc tính "type" là "text" thì password đang được hiển thị
    
    def login(self, email, password): #hàm login với email và password được truyền vào
        self.input_email(email)
        self.input_password(password)
        self.click(self.login_button)