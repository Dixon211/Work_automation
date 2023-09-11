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

print (client_ids)
#use client Id's to get information from all U+C
the_list ={}


for client_id in client_ids:
    list_of_employees = []
    #error catching
    try:
    #connecting
        temp = sesh.get(f'https://portal.shipshapeit.com/{client_id}/Users_and_Computers', cookies=cookies)
        if temp.status_code == 200:
            print(f"connected to {client_id}")
            soup = bs4(temp.content, "html.parser")
            table = soup.find("table", class_="table1 sortable")
            tr_list = table.find_all("tr")

            #walking the tree
            for tr in tr_list:
                tds = tr.find_all("td")


                td_list = []
                for td in tds:
                    td_txt = td.get_text()
                    td_list.append(td_txt)

                #cleanup and formatting
                imp_info = []
                for x in td_list:
                    if x =='\xa0':
                        pass
                    else:
                        if len(imp_info) < 2:
                            imp_info.append(x)
                        else:
                            if '@' in x:
                                imp_info.append(x)
                                break
                
                bad_words = ['computer', 'Computer', 'laptop', "Laptop", 'machine', 'Machine']
                list_formatted = {}
                for i, x in enumerate(imp_info):
                    if '\xa0' in x:
                        imp_info[i] = x.replace('\xa0', '')
                
                for x in imp_info:
                    if x in bad_words  or len(imp_info) < 3:
                        break
                    else:
                        list_formatted['lname'] = imp_info[0]
                        list_formatted['fname'] = imp_info[1]
                        list_formatted['email'] = imp_info[2]

                if list_formatted == {}:
                    pass
                else:    
                    list_of_employees.append(list_formatted) 

        #finally
        the_list[client_id] = list_of_employees



                


                
            

    except requests.exceptions.RequestException as req_exc:
        print("Request Exception:", req_exc)
    except Exception as e:
        print("An error occurred", e)


with open("./clients.json", "w") as json_file:
    json.dump(the_list, json_file)

sesh.close()