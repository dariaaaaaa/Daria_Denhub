from behave import given, when, then, step
from features.lib.pages.login_page import LoginPage
from features.lib.pages.dashboard_page import DashboardPage
from features.lib.pages.admin_page import AdminPage
from features.lib.pages.jobtitle_list_page import JobTitleListPage
from features.lib.pages.save_jobtitle_page import SaveJobTitlePage


@given(u'the user logging in with username and password given on the page')
def logging(context):
    page = LoginPage(context)
    page.visit("https://opensource-demo.orangehrmlive.com/index.php/auth/login")
    username, password = page.get_credentials()
    login = page.signin(username, password)


@step(u'navigates to Admin')
def go_to_admin(context):
    DashboardPage(context).admin.click()


@step(u'navigates to to Job - Job Titles')
def go_to_job(context):
    page = AdminPage(context)
    page.job.click()
    page.job_title.click()


@given(u'there is no "{title}" record on the grid')
def check(context, title):
    page = JobTitleListPage(context)
    if page.contains_content(title):
        page.select_checkbox(title)
        page.delete_record()


@step(u'user click on the Add button')
def add(context):
    JobTitleListPage(context).add.click()


@given(u'fill the fields with following')
def fill_fields(context):
    page = SaveJobTitlePage(context)
    page.fill_job_info(context.table.rows[0])


@when(u'user click on Save')
def save(context):
    SaveJobTitlePage(context).save.click()


@then(u'newly added title "{title}" is visible on the grid')
def check(context, title):
    page = JobTitleListPage(context)
    assert page.contains_content(title)


@given(u'user has already created job title "{title}"')
def add(context, title):
    page = JobTitleListPage(context)
    if not page.contains_content(title):
        page.add.click()
        next_page = SaveJobTitlePage(context)
        next_page.fill_job_info({'job_title': title,
                                 'description': "",
                                 'notes': ""})
        next_page.save.click()


@when(u'user fills the Job Title field with "{title}"')
def try_to_fill(context, title):
    page = SaveJobTitlePage(context)
    page.fill_job_info({'job_title': title,
                        'description': "",
                        'notes': ""})


@then(u'error message "{error}" appear')
def check_error(context, error):
    page = SaveJobTitlePage(context)
    assert page.contains_error(error)


@given(u'the following existing record')
def go_to_job(context):
    record = (context.table.rows[0])['job_title']
    page = JobTitleListPage(context)
    if not page.contains_content(record):
        page.add.click()
        next_page = SaveJobTitlePage(context)
        next_page.fill_job_info({'job_title': record,
                                 'description': "",
                                 'notes': ""})
        next_page.save.click()


@step(u'user select "{record}" record')
def go_to(context, record):
    page = JobTitleListPage(context)
    record_button = page.find_record(record)
    record_button.click()


@step(u'click on Edit button')
def edit(context):
    SaveJobTitlePage(context).edit.click()


@step(u'refill Job Description with "{description}"')
def refill(context, description):
    page = SaveJobTitlePage(context)
    page.edit_description(description)


@when("the user click on Save")
def save(context):
    SaveJobTitlePage(context).save.click()


@then("following changes is visible on the grid")
def check(context):
    changes = (context.table.rows[0])['new_description']
    page = JobTitleListPage(context)
    assert page.contains_content(changes)


@given("user select the following existing record")
def select(context):
    record = (context.table.rows[0])['job_title']
    page = JobTitleListPage(context)
    page.select_checkbox(record)


@when("user click on Delete button")
def delete(context):
    page = JobTitleListPage(context)
    page.delete_record()


@then("{text} record no longer visible on the grid")
def check(context, text):
    page = JobTitleListPage(context)
    assert not page.contains_content(text)
