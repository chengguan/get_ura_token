import requests

accesskey = "<paste your access key here>"

url = 'https://www.ura.gov.sg/uraDataService/insertNewToken.action'
myobj = {'AccessKey': accesskey}

resp = requests.post(url, headers=myobj)

if (resp.status_code==200):
    try:
        result = resp.json()['Result']
        print(f"Token: '{result}'.")
    except:
        print(resp.text)
else:
    print(resp.text)
