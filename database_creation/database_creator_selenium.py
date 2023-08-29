from dotenv import load_dotenv
import os
from selenium import webdriver

#load secret variables
load_dotenv()
portal_uname = os.environ.get("portal_uname")
portal_pass = os.environ.get("portal_pass")

chrome_driver_path = "C:\Program Files\Google\Chrome\Application\chrome.exe"
chrome_browser = webdriver.Chrome("C:\Program Files\Google\Chrome\Application\chrome.exe")

#selenium login
chrome_browser = webdriver.Chrome(executable_path=chrome_driver_path)

uname_box = chrome_browser.find_element_by_name("username")
uname_box.send_keys(portal_uname)

pword_box = chrome_browser.find_element_by_name("password")
pword_box.send_keys(portal_pass)

login_btn = chrome_browser.find_element_by_name("deki_buttons[action][login]")
login_btn.click()

current_url = chrome_browser.current_url
print(current_url)