from flask import Flask    
import requests
from requests.auth import HTTPBasicAuth
import json
import os
app = Flask(__name__)

# @app.route("/createJIRA")  # This is not a get type, it's a POST, so we need to specify the method :
@app.route("/createJIRA", methods=['POST'])
def createJIRA():        # get entire content from createJira 014
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
                "type": "text"
                }
            ],
            "type": "paragraph"
            }
        ],
        "type": "doc",
        "version": 1
        },
        "project": {
        "key": "RAT"
        },
        "issuetype": {
        "id": "10011"
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

    return json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": "))

app.run('0.0.0.0', port=5000)


# Run this flask on your ec2
 
# Now this will accept the reqeusts from the github
# and create a webHook with
# http://serverIP:5000/createJIRA