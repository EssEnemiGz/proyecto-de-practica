from flask import Flask, render_template
from dotenv import load_dotenv
import libsql_experimental as libsql
import os

# MICRO SERVICES
import services.login as login
import services.register as register

load_dotenv()
app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY")

# Connect to db
url = "libsql://go-shopping-essenemigz.turso.io"
auth_token = os.getenv("AUTH_TOKEN")
db = libsql.connect("go-shopping.db", sync_url=url, auth_token=auth_token)
db.sync()

# REGISTER BLUEPRINTS
app.register_blueprint(login.login_bp)
app.register_blueprint(register.register_bp)

login.db = db
register.db = db

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/form')
def form():
    return render_template('form.html')
 
@app.route('/register')
def register():
    return render_template('register.html')
 

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001, threaded=True)