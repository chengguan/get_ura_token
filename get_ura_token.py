# get_ura_token.py
# 19 May 2020
#
# Register for your access key here: https://www.ura.gov.sg/maps/api/reg.html
# Questions or bugs, please write to chengguan.teo@gmail.com.
import requests

# Paste your access key from URA here. THe access key is valid for 1 year.
accesskey = "<paste your access key here>"

url = 'https://www.ura.gov.sg/uraDataService/insertNewToken.action'
myobj = {'AccessKey': accesskey}

# Place the access key in the request header and send.
resp = requests.post(url, headers=myobj)

if (resp.status_code==200):
    try:
        result = resp.json()['Result']
        print(f"Token: '{result}'.")
    except:
        print(resp.text) # print error msg (should the resp data structure changed...)
else:
    print(resp.text) # print error msg
