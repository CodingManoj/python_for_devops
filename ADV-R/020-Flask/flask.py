from flask import Flask          # Just importing flask from the entire package
# app = Flask(__name__)            # To initiate flask : flask is just a frameWork for python

app = Flask(__name__,
            static_url_path='', 
            static_folder='./',)

app.run('0.0.0.0', port=5001) 
