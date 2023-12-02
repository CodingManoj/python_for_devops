# Google ---> Mail Over API ( SendInBlue is now brevo ) : 
# Create an account in Brevo
# Hit Brevo, send email over Bravo and copy the curl command, convert curl to python code online
# API Call To Brevo : https://developers.brevo.com/docs/send-a-transactional-email
# camelSensitive for keys doesn't work sometimes.

import requests
import sys
import json
apikey=sys.argv[1]
# apiKey= 


headers = {
    'accept': 'application/json',
    'api-key': apikey,
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
            'name': 'TheCloudCareers YouTube Channel',
        },
    ],
    'subject': '1129 I am email from Bravo',
    'htmlContent': '<html><head></head><body><p>1131Brevo,sending at 1129</p>This is my first transactional email sent from Brevo.</p></body></html>'
}

response = requests.post('https://api.brevo.com/v3/smtp/email', headers=headers, json=json_data)
print(json.dumps(response.status_code))