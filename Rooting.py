import requests
import json
from requests.api import request
from requests.models import Response
import re



r = requests.session()

green_color = "\033[1;32m"
red_color = "\033[1;31m"
detect_color = "\033[1;34m"
banner_color = "\033[1;33;40m"
end_banner_color = "\33[00m"

print (detect_color+"""
    ███████ ███████  ██████  ███    ███               ██████   ██████   ██████  ████████
       ██   ██       ██   ██ ████  ████               ██   ██ ██    ██ ██    ██    ██
       ██   █████    ███████ ██ ████ ██     █████     ██████  ██    ██ ██    ██    ██   
       ██   ██       ██   ██ ██  ██  ██               ██   ██ ██    ██ ██    ██    ██ 
       ██   ███████  ██   ██ ██      ██               ██   ██  ██████   ██████     ██
      
                                                                                     
     ██████  ██ ██████  ██████         █████  ██      ██████  ██    ██  ██████  ██        
     ██   ██ ██      ██ ██   ██       ██   ██ ██      ██   ██ ██    ██ ██    ██ ██        
     ██████  ██  █████  ██   ██ █████ ███████ ██      ██████  ██    ██ ██    ██ ██        
     ██   ██ ██ ██      ██   ██       ██   ██ ██      ██   ██ ██    ██ ██ ▄▄ ██ ██        
     ██   ██ ██ ███████ ██████        ██   ██ ███████ ██   ██  ██████   ██████  ██       
                                                                   ▀▀       
                                                                                                                                               
                                                                                           
""")
print (end_banner_color + '''
==============================================
Powerd By TEAM-ROOT Created By : RiadAlruqi 
==============================================
''')







r = requests.session()




number = input("ادخل الرقم بدون 0 => ")
while not number.isdigit():
    number = input("الرجاء إدخال أرقام فقط. ادخل الرقم بدون 0 => ")

data = {
    "number": "966" + number,
}

def Riad(url, data, header):
    response = requests.post(url, data=data, headers=header).text
    response = re.sub('[,]+', '', response)
    response = '\n'.join(response.replace('\n', '').replace('num', '').replace('name', '').replace('', '').split('{'))
    response = response.replace('"', '')
    return response
url = "http://86.48.0.204:919/main/"
header = {
    "Content-Type": "application/x-www-form-urlencoded; charset=utf-8",
    "User-Agent": "%D9%86%D9%85%D8%A8%D8%B1%D8%A8%D9%88%D9%83%20%D8%A7%D9%84%D8%AE%D9%84%D9%8A%D8%AC%201/3.3 CFNetwork/1240.0.4 Darwin/20.5.0",
    "Accept-Encoding": "gzip, deflate",
    "Host": "86.48.0.204:919",
    "Accept": "*/*",
    "Accept-Language": "ar",
    "Authorization": "Basic aW9zYWRtaW46cGFzc3BvcmQ=",
    "token": "pcfgv64567ko1",
    "Content-Length": str(len(number) +0),
}
response = Riad(url, data, header)
print(response)
