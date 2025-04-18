from behave import *

@given(u'I navigated to Login page')
def step_impl(context):
  print("Inside - I navigated to Login page")


@when(u'I enter valid email address and valid password into the fields')
def step_impl(context):
    print("Inside - I enter valid email address and valid password into the fields")


@when(u'I click on Login button')
def step_impl(context):
    print("Inside - I click on Login button")


@then(u'I should get logged in')
def step_impl(context):
    print("Inside - Then I should get logged in")


@given(u'I navigate to Login page')
def step_impl(context):
    print("Inside - I navigate to Login page")


@when(u'I enter invalid email and valid password into the fields')
def step_impl(context):
    print("When I enter invalid email and valid password into the fields")


@then(u'I should get a proper warning message')
def step_impl(context):
    print("Inside - I should get a proper warning message")


@when(u'I enter valid email and invalid password into the fields')
def step_impl(context):
    print("Inside - I enter valid email and invalid password into the fields")


@when(u'I enter invalid email and invalid password into the fields')
def step_impl(context):
    print("Inside - I enter invalid email and invalid password into the fields")


@when(u'I dont enter anything email and password fields')
def step_impl(context):
    print("Inside - I dont enter anything email and password fields")