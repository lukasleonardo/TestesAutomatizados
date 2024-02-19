from behave import *
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

@given('that i launch the browser.')
def LaunchBrowser(context):
    service = Service(ChromeDriverManager().install())
    context.driver = webdriver.Chrome(service=service)
    


@when('I enter the login page.')
def LaunchLoginPage(context):
    context.driver.get("https://www.saucedemo.com")
    


@when('insert a "{username}" and "{password}"')
def InputData(context,username,password):
    context.driver.find_element('xpath','/html/body/div/div/div[2]/div[1]/div/div/form/div[1]/input').send_keys(username)
    context.driver.find_element('xpath','/html/body/div/div/div[2]/div[1]/div/div/form/div[2]/input').send_keys(password)

@when('click the button login.')
def Login_btn(context):
    context.driver.find_element('xpath','/html/body/div/div/div[2]/div[1]/div/div/form/input').click()


@then('It should display the products catalog.')
def AssertLogin(context):
    content = context.driver.find_element('xpath','/html/body/div/div/div/div[1]/div[2]/span').text
    assert content == "Products"
    context.driver.close()
   
    
