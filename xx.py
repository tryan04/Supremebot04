catagory = input('Catagory: ')
YourKeyword = input('Keyword: ')
YourColor = input('Color: ')
YourSize = input('Size: ')
YourName = input('First and Last Name: ')
YourEmail = input('Email: ')
YourPhone = input('Phone Number: ')
YourAddress  = input('Address: ')
YourZip = input('Zipcode: ')
YourCity = input('City: ')
state = input('State: ')
card = input('Who is your credit card provider?')
def card_provider(card):
    if card.lower() == 'mastercard':
        return 'Mastercard'
    elif card.lower() == 'visa':
        return 'Visa'
    elif card.lower() == 'american express':
        return 'American Express'
    else:
        return 'Your card provider is not an accepted payment method.'
    
number = input('What is your credit card number?')
YourCVV = input('CVV: ')
month = input('What is the expiration month?')
year = input('What is the expiration year?')

import time
import requests
import selenium
from selenium import webdriver
from selenium.webdriver.support.ui import Select
chrome_path = r"C:\Users\Ed McFadden\Desktop\chromedriver_win32 (8)\chromedriver.exe"
driver = webdriver.Chrome(chrome_path)
driver.get(r"http://www.supremenewyork.com/shop/all/%s" % catagory)
driver.implicitly_wait(3)
color = driver.find_element_by_id('container')
for option in color.find_elements_by_tag_name('h1'):
    if option.text == str(YourKeyword):
        option.click()
driver.find_element_by_xpath("//select[@name='s']/option[text()='%s']" % YourSize).click()
driver.find_element_by_xpath("""//*[@id="add-remove-buttons"]/input""").click()
time.sleep(1)
driver.get(r'https://www.supremenewyork.com/checkout')
name = driver.find_element_by_xpath("""//*[(@id = "order_billing_name")]""")
name.send_keys(str(YourName))
email = driver.find_element_by_xpath("""//*[(@id = "order_email")]""")
email.send_keys(str(YourEmail))
phone = driver.find_element_by_xpath("""//*[(@id = "order_tel")]""")
num = YourPhone
phone.send_keys(str(num))
address = driver.find_element_by_xpath("""//*[@id="bo"]""")
address.send_keys(str(YourAddress))
zipcode = driver.find_element_by_xpath("""//*[@id="order_billing_zip"]""")
zip_code = (str(YourZip))
zipcode.send_keys(str(zip_code))
city = driver.find_element_by_xpath("""//*[@id="order_billing_city"]""")
city.send_keys(str(YourCity))
state = driver.find_element_by_xpath("""//*[@id="order_billing_state"]/option[text()='IL']""").click()
credit_num = driver.find_element_by_xpath("""//*[@id="nnaerb"]""")
creditNumber = number
credit_num.send_keys(str(creditNumber))
ex_month = driver.find_element_by_xpath("""//*[@id="credit_card_month"]/option[text()='%s']""" % month).click()
ex_year = driver.find_element_by_xpath("""//*[@id="credit_card_year"]/option[text()='%s']""" % year).click()
cvv = driver.find_element_by_xpath("""//*[@id="orcer"]""")
cvv.send_keys(str(YourCVV))
driver.find_element_by_xpath("""//*[@id="cart-cc"]/fieldset/p[2]/label/div/ins""").click()
driver.find_element_by_xpath("""//*[@id="pay"]/input""").click()
