from .base_page import BasePage
from selenium.webdriver.common.by import By


class SaveJobTitlePage(BasePage):
    def __init__(self, context):
        BasePage.__init__(self, context.browser,
                          base_url='https://opensource-demo.orangehrmlive.com/index.php/admin/')

    locator_dictionary = {
        "save": (By.NAME, "btnSave"),
        "edit": (By.NAME, "btnSave"),
        "job_title": (By.ID, "jobTitle_jobTitle"),
        "job_description": (By.ID, "jobTitle_jobDescription"),
        "job_notes": (By.ID, "jobTitle_note")
    }

    def fill_job_info(self, fields):
        self.job_title.send_keys(fields['job_title'])
        self.job_description.send_keys(fields['description'])
        self.job_notes.send_keys(fields['notes'])

    def edit_description(self, new_description):
        self.job_description.clear()
        self.job_description.send_keys(new_description)
