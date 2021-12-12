from selenium import webdriver
import logging
import os


def before_all(context):
    path = os.getcwd() + '/features/lib/chromedriver'
    driver = webdriver.Chrome(executable_path=path)
    driver.maximize_window()
    driver.implicitly_wait(10)

    context.browser = driver


def after_all(context):
    print("============ That's all folks ============")
    context.browser.close()
