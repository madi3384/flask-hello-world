import psycopg2
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World from Mathew Di Stadio in 3308'

@app.route('/db-test')
def test():
    conn = psycopg2.connect ("postgresql://basketball_nmkt_user:vuU6ZLrvQdrqzxcVtVTJEVG4LT6xhWgl@dpg-cvlihe7gi27c73e3qco0-a/basketball_nmkt")
    conn.close()
    return "Database Connection Successful"
