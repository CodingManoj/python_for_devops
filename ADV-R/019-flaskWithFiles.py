# Scenario : We want to fetch the information of our AWS Account Resources and display that.
# And also I don't have access to AWS Console On Production Account as I am consultant and I don't have access, how can we do that ??? 
# This can be achieved with python ( list of ec2, ecr, eks or anything of our choice ) and we want this info to be accessed by the other teammates using NGINX.

# First, let's serve the sample application using sample hello world.
# Google ---> Python Hello World Web Program
# ( Let's deploy an application on flast )

# let's run a sample flask
# pip3 install flask

# We want to serve the web content from a file
# Google ---> How to server static files : https://stackoverflow.com/questions/20646822/how-to-serve-static-files-in-flask
# app = Flask(__name__,
#             static_url_path='', 
#             static_folder='web/static',
#             template_folder='web/templates')


from flask import Flask          # Just importing flask from the entire package
# app = Flask(__name__)            # To initiate flask : flask is just a frameWork for python
app = Flask(__name__,
            static_url_path='', 
            static_folder='./')


@app.route("/")                  # Decorator to accept only requests on / 
def hello():
    return 'Sample Flask App'

app.run('0.0.0.0', port=5001) 
