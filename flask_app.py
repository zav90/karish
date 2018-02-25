# A very simple Flask Hello World app for you to get started with...

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["DEBUG"] = True

SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://{zav90}:{password}@{hostname}/{databasename}".format(
    username="zav90",
    password="1qazxsw@",
    hostname="zav90.mysql.pythonanywhere-services.com",
    databasename="zav90$ZavDB",
)
app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
app.config["SQLALCHEMY_POOL_RECYCLE"] = 299
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

@app.route('/')
def hello_world():
    return 'Hello from Flask suka !'


if __name__ == '__main__':
    app.run()

