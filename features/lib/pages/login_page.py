from .base_page import BasePage
from selenium.webdriver.common.by import By


class LoginPage(BasePage):
    def __init__(self, context):
        BasePage.__init__(self, context.browser,
                          base_url='https://opensource-demo.orangehrmlive.com/index.php/auth/login')

    locator_dictionary = {
        "credentials": (By.XPATH, '//span[contains(text(), "Username")]'),
        "username_field": (By.NAME, 'txtUsername'),
        "password_field": (By.NAME, 'txtPassword'),
        "submit": (By.NAME, 'Submit')
    }

    def get_credentials(self):
        credentials = (self.credentials.text).rstrip().split()
        return credentials[3], credentials[-2]

    def signin(self, username, password):
        self.username_field.send_keys(username)
        self.password_field.send_keys(password)
        login = self.submit.click()
        return login
