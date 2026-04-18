class BasePage:
    def __init__(self, page):
        self.page = page

    #hàm điều hướng đến một URL cụ thể bằng cách sử dụng phương thức goto() của Playwright với URL được truyền vào
    def navigate(self, url):
        self.page.goto(url)

    #hàm click vào một phần tử được xác định bởi selector bằng cách sử dụng phương thức click() của Playwright với selector được truyền vào
    def click(self, selector):
        self.page.click(selector)

    #hàm điền vào một trường input được xác định bởi selector với giá trị text
    def fill(self, selector, text):
        self.page.fill(selector, text)

    #hàm lấy văn bản của một phần tử được xác định bởi selector bằng cách sử dụng phương thức text_content() của Playwright
    def get_text(self, selector):
        return self.page.text_content(selector)

    #hàm lấy giá trị hiện tại của một trường input được xác định bởi selector
    def get_input_value(self, selector): 
        return self.page.input_value(selector)
    
    #hàm lấy giá trị của một thuộc tính cụ thể của một phần tử được xác định bởi selector bằng cách sử dụng phương thức get_attribute() của Playwright với selector và tên thuộc tính được truyền vào
    def get_attribute(self, selector, attribute): 
        return self.page.get_attribute(selector, attribute)

    #hàm kiểm tra xem một đoạn văn bản cụ thể có hiển thị trên trang hay không bằng cách sử dụng phương thức is_visible() của Playwright với selector được truyền vào
    def is_text_visible(self, text): 
        return self.page.is_visible(f"text={text}")
    
    #hàm kiểm tra xem một phần tử cụ thể có hiển thị trên trang hay không bằng cách sử dụng phương thức is_visible() của Playwright với selector được truyền vào
    def is_element_visible(self, selector): 
        return self.page.is_visible(selector)
    
    #hàm kiểm tra xem một phần tử cụ thể có bị vô hiệu hóa hay không bằng cách sử dụng phương thức is_disabled() của Playwright với selector được truyền vào
    def is_element_disabled(self, selector):
        return self.page.is_disabled(selector)
    