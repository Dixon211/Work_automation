import requests
from dotenv import load_dotenv
import os
from bs4 import BeautifulSoup as bs4

#load secret variables
load_dotenv()
portal_uname = os.environ.get("portal_uname")
portal_pass = os.environ.get("portal_pass")

#create and login to session
sesh = requests.Session()

#session info
portal_li_url = 'https://portal.shipshapeit.com/index.php?title=Special:Userlogin'
portal_payload = {'username': portal_uname, 'password': portal_pass, "auth_id": 1, "deki_buttons[action][login]": "login"}

response = sesh.post(portal_li_url, data=portal_payload)


if response.status_code == 200:
    print("I'm in")
    access = True
else:
    print("Login Failed")

if access == True:
   html_content = response.content
   bs4_html = bs4(html_content, "html.parser")
   client_divs = bs4_html.find_all("div", cd= "0")
   client_ids = []

   for div in client_divs:
       for attr_name, attr_value in div.attrs.items():
           if "path" in attr_name and len(attr_value) == 4:
               better_value = attr_value.split("/")
               client_ids.append(better_value[0])

print(client_ids)







sesh.close()