import json

import requests

URL = "http://127.0.0.1:8000/stucreate/"

data = {
    'name' : 'Konam',
    'roll' : 102,
    'city' : 'Kachi'
}

json_data = json.dumps(data)
r = requests.post(url = URL, data = json_data)


data = r.json()
print(data)

