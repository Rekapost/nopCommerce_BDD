from selenium.webdriver.common.by import By
from behave import *
from selenium import webdriver

@given('Launch Chrome browser')
def launchbrowser(context):
    context.driver=webdriver.Chrome()

@when('Open nopCommerce page')
def openpage(context):
    context.driver.get("https://admin-demo.nopcommerce.com")

@when('Enter username "{user}" and password "{pwd}"')
def entercredentials(context,user, pwd):
    context.driver.find_element(By.XPATH,"//input[@id='Email']").clear()
    context.driver.find_element(By.XPATH,"//input[@id='Email']").send_keys(user)

    context.driver.find_element(By.XPATH,"//input[@id='Password']").clear()
    context.driver.find_element(By.XPATH,"//input[@id='Password']").send_keys(pwd)

@when('Click on login button')
def loginpage(context):
    context.driver.find_element(By.XPATH,"//button[normalize-space()='Log in']").click()

@then('User must be successfully able to login to dashboard page')
def dashboardpage(context):
    status=context.driver.title
    try:
        text=context.driver.find_element(By.XPATH,"//h1[normalize-space()='Dashboard']").text
    except:
        context.driver.close()
        assert False, "Test Failed"

    if status=="Dashboard / nopCommerce administration":
        context.driver.close()
        assert True,"Test Passed"

@then('Close browser')
def closebrowser(context):
    context.driver.close()


#  terminal:   behave features\nopcommerce.feature

#  terminal:   behave -f allure_behave.formatter:AllureFormatter -o reports/ features

#  terminal:   allure serve reports/
