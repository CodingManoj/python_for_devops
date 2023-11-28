# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
from requests.auth import HTTPBasicAuth
import json
import os

url = "https://impachigolla.atlassian.net/rest/api/3/issue"

API_TOKEN=os.getenv('TOKEN')

auth = HTTPBasicAuth("impachigolla1992@gmail.com", API_TOKEN)

headers = {
  "Accept": "application/json",
  "Content-Type": "application/json"
}

payload = json.dumps( {
  "fields": {
    "description": {
      "content": [
        {
          "content": [
            {
              "text": "Jira Ticket From Py Script",
              "type": "Jira Ticket From Py Script"
            }
          ],
          "type": "paragraph"
        }
      ],
      "type": "doc",
      "version": 1
    },
    "project": {
      "key": "PD"
    },
    "issuetype": {
      "id": "10006"
    },
    "summary": "Jira Ticket From Py Script",
  },
  "update": {}
} )

response = requests.request(
   "POST",
   url,
   data=payload,
   headers=headers,
   auth=auth
)

print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))