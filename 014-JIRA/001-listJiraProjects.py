# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests                              # Importing Requests Package
from requests.auth import HTTPBasicAuth      # Importing HTTPBasciAuth Module for establishing authentication with app
import json
import os 

url = "https://impachigolla.atlassian.net/rest/api/3/project"

API_TOKEN=os.getenv('TOKEN')

auth = HTTPBasicAuth("impachigolla1992@gmail.com", API_TOKEN)

headers = {
  "Accept": "application/json"
}

response = requests.request(                 #  requests module is to establish authentication and authorization!!!
   "GET",
   url,
   headers=headers,
   auth=auth
)

# print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))
# Python offers the output as list, we need to convert that to dictionary then only we can make things queryable
# print(response)
output=json.loads(response.text)       #  json.loads() Converts list to a json, so that we can query


project_name=output[1]["name"]
print("Name Of The Project:", project_name)