# Goal : If someone in the internet hits my app, it just has to respond back with "Hello World
# flask is a very big package, I just want Flask module ( just to increase the load time )

from flask import Flask    

# This is a common line and this creates FLASK APPLICATION INSTANCE.
app = Flask(__name__)

# Anything that starts with @ is a decorator

# This is a usual program
# def hello():
#     return "HELLO WORLD"

# hello()

# What is a decorator in python ? Anything that starts with @ is referred as decorator
# Decorator is like a Role Dependency in Ansible, usually decorators are placed just above the functions.
# If someone invokes a function, first that decorator will be executed first.

# If someone wants to access an ratingsFunction, I want this to be accessed only if he as Authorization and in the decorator we will say that

# Flask is like a SPRING BOOT Framework which offers in-built webServer


# If any calls hello() function, the it will only be processed if the endPoint of the call is / , if you give it as /ec2, flast won't let the function call happen
@app.route("/")
def hello():
    return "HELLO WORLD"


# Run's this application on the below IP and available to internet ! Better execute this on EC2
app.run('0.0.0.0') 

# Just run the app 
# python 001-helloWorld.py  # you can access this app from EC2IP:5000/  and if you give anything apart from trailing slash, it won't work.
# python3 helloworld.py

#  * Serving Flask app 'helloworld' (lazy loading)
#  * Environment: production
#    WARNING: This is a development server. Do not use it in a production deployment.
#    Use a production WSGI server instead.
#  * Debug mode: off
#  * Running on all addresses.
#    WARNING: This is a development server. Do not use it in a production deployment.
#  * Running on http://172.31.42.225:5000/ (Press CTRL+C to quit)

# http://172.31.42.225:5000/      ( Gives helloWorld response back )
# http://172.31.42.225:5000/blah  ( Flask says use correct endPoint , technically Decorator )

# Decorator is saying to accept only the reqeusts that comes on / and don 't take any other requests.

# By default flask runs on port 5000, if you want to change it, we can it 
