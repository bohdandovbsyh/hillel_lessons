import allure
from selenium.webdriver.common.by import By

from framework_from_scratch.utilities.decorators import auto_steps
from framework_from_scratch.utilities.web_ui.base_page import BasePage


@auto_steps
class LoginPage(BasePage):
    __email_input = (By.XPATH, "//input[@id='email']")
    __password_input = (By.XPATH, '//input[@id="passwd"]')
    __login_button = (By.XPATH, '//*[@id="SubmitLogin"]')

    def __init__(self, driver):
        super().__init__(driver)

    def set_user_email(self, email):
        self.send_keys(self.__email_input, email)
        return self

    def set_password(self, password):
        self.send_keys(self.__password_input, password)
        return self

    def click_login_button(self):
        self.click(self.__login_button)
        return self

    def login(self, email, password):
        self.set_user_email(email)
        self.set_password(password)
        self.click_login_button()
        return self
