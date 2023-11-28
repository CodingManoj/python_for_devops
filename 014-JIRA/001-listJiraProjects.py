# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests                              # Importing Requests Package
from requests.auth import HTTPBasicAuth      # Importing HTTPBasciAuth Module for establishing authentication with app
import json

url = "https://impachigolla.atlassian.net/rest/api/3/project"

API_TOKEN="ATATT3xFfGF0rcMsyrbwA48hJrPmi8IilSO-bTOc9BS9H0dKU4LyvzJoYds6s30jLOknIjmbO42SNITxnymDziG2DPhB3LWtvi-Stlhs3GieCVwHw9Ni3QtJAZ1gjUaHWNhswFHuU5CLCgxO5vS76u5Xh_F2BlwX0XHciVQufw51Px7lPk6pNiE=39BCB547"


auth = HTTPBasicAuth("impachigolla1992@example.com", API_TOKEN)

headers = {
  "Accept": "application/json"
}

response = requests.request(
   "GET",
   url,
   headers=headers,
   auth=auth
)

print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))