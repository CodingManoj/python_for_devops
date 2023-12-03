from flask import Flask          

app = Flask(__name__,
            static_url_path='', 
            static_folder='./',)

app.run('0.0.0.0', port=5001) 
