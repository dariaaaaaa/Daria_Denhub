from .base_page import BasePage
from selenium.webdriver.common.by import By


class JobTitleListPage(BasePage):
    def __init__(self, context):
        BasePage.__init__(self, context.browser,
                          base_url='https://opensource-demo.orangehrmlive.com/index.php/admin/')

    locator_dictionary = {
        "add": (By.NAME, "btnAdd"),
        "delete": (By.NAME, "btnDelete"),
        "confirm": (By.ID, "dialogDeleteBtn")
    }

    def select_checkbox(self, record_name):
        path = '//a[text()="' + record_name + '"]'
        record_href = self.find((By.XPATH, path)).get_attribute('href')
        value = record_href[(record_href.index('=') + 1)::]
        s = "ohrmList_chkSelectRecord_" + str(value)
        self.find((By.ID, s)).click()

    def delete_record(self):
        self.delete.click()
        self.confirm.click()

    def find_record(self, record):
        path = '//a[text()="' + record + '"]'
        return self.find((By.XPATH, path))
