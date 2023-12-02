# Google ---> Mail Over API ( SendInBlue is now brevo ) : 
# Create an account in Brevo
# Hit Brevo, send email over Bravo and copy the curl command, convert curl to python code online
# API Call To Brevo : https://developers.brevo.com/docs/send-a-transactional-email

import requests
import sys 
import json
apiKey=sys.argv[1]


headers = {
    'accept': 'application/json',
    'api-key': 'apiKey',
    'content-type': 'application/json',
}

json_data = {
    'sender': {
        'name': 'IMPachigolla',
        'email': 'impachigolla@gmail.com',
    },
    'to': [
        {
            'email': 'thecloudcareers@gmail.com',
            'name': 'TheCloudCareers',
        },
    ],
    'subject': 'I am email from Bravo',
    'htmlContent': '<html><head></head><body><p>Hello, I am fro  Brevo</p>This is my first transactional email sent from Brevo.</p></body></html>',
}

response = requests.post('https://api.brevo.com/v3/smtp/email', headers=headers, json=json_data)
print(json.dumps(response)) 

