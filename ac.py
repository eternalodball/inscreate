#!/usr/bin/python3

import sys , os , random , requests , time
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.proxy import Proxy , ProxyType
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from http_request_randomizer.requests.proxy.requestProxy import RequestProxy
from webdriver_manager.chrome import ChromeDriverManager
from fake_useragent import UserAgent

#color

class color:
   PURPLE = '\033[95m'
   GREEN = '\033[92m'
   BOLD = '\033[1m'
   CWHITE  = '\33[37m'

#API

print(color.BOLD)
#YOUR_API_KEY = input(color.GREEN + '[~] ' + color.CWHITE + 'ENTER YOUR API KEY : ')
YOUR_API_KEY = "73f628e9c7msh97e06b0997fdb30p11d02djsn70d49c150b71"

#Fake useragent

options = Options()
ua = UserAgent()
userAgent = ua.random

#Proxy (highly required)

prox = Proxy()
prox.proxy_type = ProxyType.MANUAL
prox.http_proxy = "83.97.23.90:33849"
#prox.socks_proxy = "ip_addr:port"
prox.ssl_proxy = "83.97.23.90:33849"

capabilities = webdriver.DesiredCapabilities.CHROME
prox.add_to_capabilities(capabilities)


#webdriver

url = "https://www.instagram.com/accounts/emailsignup/"
CHROME_DIR = "/home/aao/Desktop/instagram/webdrivers/chromedriver"

browser = webdriver.Chrome(CHROME_DIR, chrome_options=options, desired_capabilities=capabilities)

print()
print( color.GREEN + "[+ ]" + color.CWHITE + "Using useragent as : " + userAgent)

#  ************************JUNK FILES****************************


#browser = webdriver.Firefox(executable_path= "/home/aao/Desktop/instagram/webdrivers/geckodriver")
#browser = webdriver.Remote(
#    "https://oauth-eternalodball-e5ca4:b4c4d09a-9c13-459b-a436-532f1682a311@ondemand.eu-central-1.saucelabs.com:443/wd/hub"
#);

#browser.test.allTheThings(CHROME_DVR_DIR)
#ClearCache before opening url (currently not working)

#browser.get('chrome://settings/clearBrowserData')
#browser.find_element_by_id('clearBrowsingDataConfirm').click()


# ***************************************************************



#Open ig signup url
browser.get(url)

#elements

time.sleep(4)
email = browser.find_element_by_css_selector('div.WZdjL:nth-child(4) > div:nth-child(1) > label:nth-child(1) > input:nth-child(2)')
fullname = browser.find_element_by_css_selector('div.WZdjL:nth-child(5) > div:nth-child(1) > label:nth-child(1) > input:nth-child(2)')
username = browser.find_element_by_css_selector('div.WZdjL:nth-child(6) > div:nth-child(1) > label:nth-child(1) > input:nth-child(2)')
Password = browser.find_element_by_css_selector('div.WZdjL:nth-child(7) > div:nth-child(1) > label:nth-child(1) > input:nth-child(2)')
signup_button = browser.find_element_by_css_selector('div.bkEs3:nth-child(1)')

# Create temporary email

url = "https://temporary-mail-afeg-ru.p.rapidapi.com/api/email/login@domain/request"

headers = {
'x-rapidapi-host': "temporary-mail-afeg-ru.p.rapidapi.com",
'x-rapidapi-key': YOUR_API_KEY
}

response_email = requests.request("GET", url, headers=headers)

print()
print( color.GREEN + "[!] " + color.CWHITE + "Generated Email : " + response_email.text)

#Create Random username

time.sleep(0.500)

username_file = open(os.getcwd() + "/user.txt", "r" )
lines = [line.rstrip() for line in username_file]

chose_random_username_list = random.sample(lines, k=1)

random_username_string = ''.join(chose_random_username_list)

random_username_number = str(random.randint(100000, 200000))

generated_random_username = random_username_string + random_username_number

print( color.GREEN + "[!] " + color.CWHITE +"Generated username = " + generated_random_username)

#Create random password to avoid detection (not really required)

time.sleep(0.500)

chose_random_password_list = random.sample(lines, k=1)

random_password_string = ''.join(chose_random_password_list)

random_password_number = str(random.randint(1000000, 2000000))

generated_random_password = random_password_string + random_password_number

print( color.GREEN + "[!] " + color.CWHITE +"Generated password = " + generated_random_password)

#Fields to use 

my_email = response_email.text
my_fullname = 'BOT KILLER'
my_username = generated_random_username
my_password = generated_random_password

#Fill the page

email.send_keys(my_email)
fullname.send_keys(my_fullname)
username.send_keys(my_username)
Password.send_keys(generated_random_password)
time.sleep(1)
Password.send_keys(Keys.ENTER)
time.sleep(6)

#elements next page

birthday_month = browser.find_element_by_css_selector('#react-root > section > main > div > div > div:nth-child(1) > div > div.qF0y9.Igw0E.IwRSH.eGOV_._4EzTm.bkEs3.DhRcB > div > div > span > span:nth-child(1) > select > option:nth-child(9)')
birthday_day = browser.find_element_by_css_selector('#react-root > section > main > div > div > div:nth-child(1) > div > div.qF0y9.Igw0E.IwRSH.eGOV_._4EzTm.bkEs3.DhRcB > div > div > span > span:nth-child(2) > select > option:nth-child(25)')
birthday_year = browser.find_element_by_css_selector('#react-root > section > main > div > div > div:nth-child(1) > div > div.qF0y9.Igw0E.IwRSH.eGOV_._4EzTm.bkEs3.DhRcB > div > div > span > span:nth-child(3) > select > option:nth-child(26)')
birthday_next_button = browser.find_element_by_css_selector('#react-root > section > main > div > div > div:nth-child(1) > div > div.qF0y9.Igw0E.IwRSH.eGOV_._4EzTm.lC6p0.g6RW6 > button')

#Fill the page

birthday_month.click()
birthday_day.click()
birthday_year.click()
time.sleep(2)
birthday_next_button.click()

#Display countdown

print()
print(color.GREEN + "[!] " + color.CWHITE + "Waiting for otp ")

print(color.GREEN + "[!] " + color.CWHITE + "Opening mail box in 15 seconds")

for remaining in range(15, 0, -1):
    sys.stdout.write("\r")
    sys.stdout.write("{:2d} seconds remaining.".format(remaining))
    sys.stdout.flush()
    time.sleep(1)

sys.stdout.write("\rComplete!            \n")

# otp page element

fill_otp = browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div[1]/div[2]/form/div/div[1]/input')

# send mail read request

url = "https://temporary-mail-afeg-ru.p.rapidapi.com/api/messages/" + my_email + "/request"

headers = {
    'x-rapidapi-host': "temporary-mail-afeg-ru.p.rapidapi.com",
    'x-rapidapi-key': YOUR_API_KEY
    }

response = requests.get(url, headers=headers)

otp_response = response.text

# Save response to response.Text

with open("response.text","w") as file:
   file.write(str(otp_response))

# Read otp from response

otp_file = open("response.text")

lines = otp_file.readlines()

for line in lines:
    my_otp = str(line[13:19])
    print(color.GREEN + "[!] " + color.CWHITE + "OTP Recieved : " + my_otp)

# fill otp

fill_otp.send_keys(my_otp)
time.sleep(2)
fill_otp.send_keys(Keys.ENTER)

# Write generated account

print(color.GREEN + '[!] ' + color.CWHITE + 'Saving account info as account_generated.txt ')
print()
with open("account_generated.txt","a") as file:
    file.write(my_email + " : " + my_password)