import requests
from dotenv import load_dotenv
import os
from bs4 import BeautifulSoup as bs4
import json

#load secret variables
load_dotenv()
portal_uname = os.environ.get("portal_uname")
portal_pass = os.environ.get("portal_pass")

#create and login to session
sesh = requests.Session()

#session info
portal_li_url = 'https://portal.shipshapeit.com/index.php?title=Special:Userlogin'
portal_payload = {'username': portal_uname, 'password': portal_pass, "auth_id": 1, "deki_buttons[action][login]": "login"}

#connect to session
response = sesh.post(portal_li_url, data=portal_payload)
cookies = (sesh.cookies).get_dict()

if response.status_code == 200:
    print("I'm in")
    access = True
else:
    print("Login Failed")

#get client Ids from HTML
if access == True:
   html_content = response.content
   bs4_html = bs4(html_content, "html.parser")
   client_divs = bs4_html.find_all("div", cd= "0")

   #ends with all client IDs with no slash or anything, ready to be used
   client_ids = []
for div in client_divs:
       for attr_name, attr_value in div.attrs.items():
           if "path" in attr_name and len(attr_value) == 4:
               better_value = attr_value.split("/")
               client_ids.append(better_value[0])

#use client Id's to get information from all U+C
the_list ={}

for client_id in client_ids:
    try:
        temp = sesh.get(f'https://portal.shipshapeit.com/{client_id}/Users_and_Computers', cookies=cookies)
        if temp.status_code == 200:
            print(f"connected to {client_id}")
            soup = bs4(temp.content, "html.parser")
            tbody = soup.find('tbody')
            tr = tbody.find_all("tr")
            for tr_single in tr:
                tds = []
                td = tr_single.find_all('td')
                for td_element in td:
                    td_txt = td_element.get_text()
                    tds.append(td_txt)
                imp_info = []
                for x in tds:
                    if x == "\xa0":
                        pass
                    else:
                        if len(imp_info) < 3:
                            imp_info.append(x)
                        else:
                            if "@" in x:
                                imp_info.append(x)
                                break
                print(imp_info)
                

                

                        

            

    except requests.exceptions.RequestException as req_exc:
        print("Request Exception:", req_exc)
    except Exception as e:
        print("An error occurred", e)



sesh.close()