import requests

url = "https://account.kudisms.net/api/?username=abayomiogunnusi@gmail.com&password=Bassguitar1&message=test&sender=Spaceet&mobiles=2348168623014"

payload={}
headers = {}

def sendSms(url, payload, headers):
    response = requests.request("POST", url, headers=headers, data=payload)

    return response.text

sendSms(url, payload, headers)

