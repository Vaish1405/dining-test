import requests
import http.client
import json

api_url = "https://api.dineoncampus.com/v1/locations/status?site_id=5efb645cbf31720ae5755e2d&timestamp=2024-11-05"

titles = []
status = []
label = []
status_message = []

# try: 
#     response = requests.get(api_url)
#     response.raise_for_status()

#     data = response.json()
# except requests.exceptions.RequestException as e:
#     print(e)

# if data:
#     for location in data.get("locations", []):
#         locations.append(location.get('name'))

conn = http.client.HTTPSConnection("api.dineoncampus.com")
conn.request("GET", "/v1/locations/status?site_id=5efb645cbf31720ae5755e2d&platform=0")
resp = conn.getresponse()
body_str = resp.read().decode("utf-8")
body = json.loads(body_str)

for location in body['locations']:
    titles.append(location['name'])
    label.append(location['status']['label'])
    status_message.append(location['status']['message'])



print(titles)
print(status)
print(label)
print(status_message)