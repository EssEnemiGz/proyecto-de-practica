from flask import Flask, render_template

app = Flask(__name__)

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
    app.run(debug=True, host='0.0.0.0', threaded=True)