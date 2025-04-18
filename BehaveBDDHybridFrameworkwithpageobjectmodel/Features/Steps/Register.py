from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By

@given(u'I navigate to Register page')
def step_impl(context):
    print("Inside - I navigate to Register page")

@when(u'I enter details into mandatory fields')
def step_impl(context):
    print("Inside - I enter details into mandatory fields")


@when(u'I click on Continue button')
def step_impl(context):
    print("Inside - I click on Continue button")


@then(u'Account should get created')
def step_impl(context):
    print("Inside - I Account should get created")

@when(u'I enter details into all fields')
def step_impl(context):
    print("Inside - I enter details into all fields")

@when(u'I enter details into all fields expect email field')
def step_impl(context):
    print("Inside - I enter details into all fields expect email field")

@when(u'I enter existing accounts email into email field')
def step_impl(context):
    print("Inside - I enter existing accounts email into email field")

@then(u'Proper warning message informing about duplicate account should be displayed')
def step_impl(context):
    print(" Inside - Proper warning message informing about duplicate account should be displayed")

@when(u'I dont enter anything into the fields')
def step_impl(context):
   print("Inside - I enter anything into the fields")

@then(u'Proper warning messages for every mandatory fields should be displayed')
def step_impl(context):
    print("Inside - Proper warning messages for every mandatory fields should be displayed")
