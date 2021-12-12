from selenium import webdriver


def before_all(context):
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)

    context.browser = driver


def after_all(context):
    print("============ That's all folks ============")
    context.browser.close()
