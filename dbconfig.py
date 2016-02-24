from flask import Flask
from flask_sqlalchemy import SQLAlchemy

localConfig = 'mysql+mysqlconnector://root:1208@127.0.0.1:3306/iam-test'
serverConfig = 'mysql://qpnfpkbur9apgsko:z2twcuglgsaycife@l3855uft9zao23e2.cbetxkdyhwsb.us-east-1.rds.amazonaws.com:3306/ofkwqg81edl8d0yd'

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = serverConfig

db = SQLAlchemy(app)