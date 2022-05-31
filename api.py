import requests

TOKEN = '###'
CHANNEL = '###'

url = "https://slack.com/api/chat.postMessage"
headers = {"Authorization": "Bearer "+TOKEN}
data  = {
   'channel': CHANNEL,
   'text': 'テストです。'
}

r = requests.post(url, headers=headers, data=data)

print("return ", r.json())