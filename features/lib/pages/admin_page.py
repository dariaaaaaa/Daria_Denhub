from .base_page import BasePage
from selenium.webdriver.common.by import By


class AdminPage(BasePage):
    def __init__(self, context):
        BasePage.__init__(self, context.browser,
                          base_url='https://opensource-demo.orangehrmlive.com/index.php/')

    locator_dictionary = {
        "job": (By.XPATH, '//a[@id="menu_admin_Job"]'),
        "job_title": (By.XPATH, '//a[@href="/index.php/admin/viewJobTitleList"]')
    }
