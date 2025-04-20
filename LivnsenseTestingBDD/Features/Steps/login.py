import csv
import os
import time
from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@given('I am on the VICAS login page')
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()
    context.driver.get("https://alv-vicas.livnsense.com/#/auth/login")
    WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'heading')]"))
    )


@then('I should see the "Welcome to VICAS" header')
def step_impl(context):
    header = context.driver.find_element(By.XPATH, "//div[contains(@class, 'heading')]")
    assert header.is_displayed()


@then('I should see the username input field')
def step_impl(context):
    username = WebDriverWait(context.driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "input#username"))
    )
    assert username.is_displayed()


@then('I should see the password input field')
def step_impl(context):
    password = WebDriverWait(context.driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "input#password"))
    )
    assert password.is_displayed()


@then('I should see the "Forgot Password?" link')
def step_impl(context):
    forgot_pwd = WebDriverWait(context.driver, 15).until(
        EC.visibility_of_element_located((By.XPATH, "//p[@class='forgot_pass']"))
    )
    assert forgot_pwd.is_displayed()


@then('I should see the "Sign in" button')
def step_impl(context):
    signin_btn = WebDriverWait(context.driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "button.sign-in-btn"))
    )
    assert signin_btn.is_displayed()
    assert signin_btn.get_attribute('disabled') is not None, "Sign in button should be disabled initially"


@when('I leave the username field empty')
def step_impl(context):
    username = WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.ID, "username"))
    )
    username.clear()
    username.send_keys(" ")


@when('I leave the password field empty')
def step_impl(context):
    password = WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.ID, "password"))
    )
    password.clear()
    password.send_keys(" ")


@then('the "Sign in" button should be disabled')
def step_impl(context):
    signin_btn = WebDriverWait(context.driver, 5).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "button.sign-in-btn"))
    )
    assert signin_btn.get_attribute('disabled') is not None, "Sign in button should be disabled when fields are empty"


@then(u'the "Sign in" button should be enabled')
def step_impl(context):
    signin_btn = WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "button.sign-in-btn"))
    )
    assert signin_btn.get_attribute('disabled') is None, "Sign in button should be enabled when both fields are filled"


@then('I should see an error message for invalid login')
def step_impl(context):
    error_msg = WebDriverWait(context.driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "div[role='alert']"))
    )
    text = error_msg.text.strip()
    assert text in ["Password is incorrect",
                    "User is not registered. Please Contact admin"], f"Unexpected error: {text}"


@given('I read login data from CSV file')
def step_impl(context):
    context.test_data = []
    csv_file_path = os.path.join(os.getcwd(), "Features", "Steps", "test_file.csv")
    with open(csv_file_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            context.test_data.append(row)


@when('I test login for each user from the CSV')
def step_impl(context):
    for row in context.test_data:
        username = WebDriverWait(context.driver, 10).until(EC.presence_of_element_located((By.ID, "username")))
        password = WebDriverWait(context.driver, 10).until(EC.presence_of_element_located((By.ID, "password")))
        signin_btn = WebDriverWait(context.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "button.sign-in-btn")))

        # Clear and enter credentials from CSV
        username.clear()
        username.send_keys(row["username"])
        password.clear()
        password.send_keys(row["password"])

        # Verify button state before clicking
        if username.get_attribute("value") and password.get_attribute("value"):
            assert signin_btn.get_attribute(
                'disabled') is None, "Sign in button should be enabled with valid credentials"
            signin_btn.click()

            # Check for error message or successful login
            time.sleep(2)
            try:
                alert = WebDriverWait(context.driver, 5).until(
                    EC.visibility_of_element_located((By.CSS_SELECTOR, "div[role='alert']"))
                )
                print(f"Login failed for ({row['username']}): {alert.text}")
            except:
                print(f"Login successful for ({row['username']})")
        else:
            assert signin_btn.get_attribute(
                'disabled') is not None, "Sign in button should be disabled with empty credentials"

        context.driver.refresh()
        WebDriverWait(context.driver, 5).until(EC.presence_of_element_located((By.ID, "username")))


def after_scenario(context, scenario):
    if hasattr(context, 'driver'):
        context.driver.quit()



@when(u'I click the "Forgot Password?" link')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I click the "Forgot Password?" link')


@then(u'I should be redirected to the password recovery page')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then I should be redirected to the password recovery page')


@when(u'I enter "invalid_user" in the username field')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I enter "invalid_user" in the username field')


@when(u'I enter "wrong_password" in the password field')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I enter "wrong_password" in the password field')


@when(u'I click the "Sign in" button')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I click the "Sign in" button')


@then(u'I should see an error message "Invalid credentials"')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then I should see an error message "Invalid credentials"')


@when(u'I enter "secret" in the password field')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I enter "secret" in the password field')


@then(u'the password field should mask the input characters')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then the password field should mask the input characters')
