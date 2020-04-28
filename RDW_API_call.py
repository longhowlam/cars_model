import requests
import pickle

tt = pickle.load(open("token.pck", "rb"))
url = "https://opendata.rdw.nl/resource/m9d7-ebf2.json?kenteken=23LJLJ"

payload = {}
headers = {
  'X-App-Token': tt
}

response = requests.request("GET", url, headers=headers, data = payload)

print(response.text.encode('utf8'))
