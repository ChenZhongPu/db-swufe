from flask import Flask
from flask import render_template
import psycopg2

# Connect to your postgres DB
conn = psycopg2.connect(host="localhost", port=5432, dbname="mydb", user="postgres", password="")

# Open a cursor to perform database operations
cur = conn.cursor()

app = Flask(__name__)

@app.route('/')
def index():
    return 'Flask with database'

@app.route('/hello/<float:value>')
@app.route('/hello/<int:value>')
def hello(value):
    sql = f'SELECT dept_name, building, budget FROM department WHERE budget > {value}'
    cur.execute(sql)
    records = cur.fetchall()
    return render_template('result.html', results=records)