from flask import Flask
from flask import render_template
from datetime import datetime
from flask import request

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/time")
def get_time():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    return f"<h1>Now is {current_time}</h1>"

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)

@app.route('/product')
def product():
    return render_template('product.html')

@app.route('/signin')
def signin():
    return render_template('signin.html')


@app.route('/display', methods=["POST"])
def display_info():
    email = request.form['email']
    pswd = request.form['password']
    return f"<p>Email: {email}, Password: {pswd}"

@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404

@app.route("/me")
def me_api():
    return {
        "name": 'zhongpu',
        "age": '29',
        "gender": 'male',
    }