from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
import traceback


class BasePage(object):

    def __init__(self, browser, base_url='https://opensource-demo.orangehrmlive.com/index.php/'):
        self.driver = browser
        self.base_url = base_url

    def __getattr__(self, elem, timeout=10):
        try:

            if elem in self.locator_dictionary.keys():
                return self.find(self.locator_dictionary[elem])

        except AttributeError:
            print(f"No {elem} here!")

    def close(self):
        self.driver.quit()

    def find(self, selector):
        return self.driver.find_element(selector[0], selector[1])

    def visit(self, url):
        self.driver.get(url)

    def contains_content(self, text, timeout=10):
        try:
            elem = WebDriverWait(self.driver, timeout).until(
                EC.text_to_be_present_in_element((By.TAG_NAME, 'body'), text))
            return elem
        except TimeoutException as ex:
            return False

