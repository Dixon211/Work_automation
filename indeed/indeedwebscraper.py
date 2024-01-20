import re
import time
from playwright.sync_api import sync_playwright

def indeedapply():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=50)
        page = browser.new_page()
        page.goto("https://secure.indeed.com/auth?hl=en_US&co=US&continue=https%3A%2F%2Fwww.indeed.com%2F&tmpl=desktop&from=gnav-util-homepage&jsContinue=https%3A%2F%2Fprofile.indeed.com%2Fonboarding%3Fhl%3Den_US%26co%3DUS%26from%3Dgnav-homepage&empContinue=https%3A%2F%2Faccount.indeed.com%2Fmyaccess")
        time.sleep(2)
        page.get_by_text("Email Address").fill("myemail@gmail.com")


indeedapply()