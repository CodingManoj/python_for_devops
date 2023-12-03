from flask import Flask    
app = Flask(__name__)

@app.route("/")
def hello():
    return 'HELLO WORLD'

app.run('0.0.0.0') 







