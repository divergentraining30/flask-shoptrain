from flask import Flask 
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__) 
app.config['SQLALCHEMY DATABASE_URI'] = 'sqlite:///myshop.db' 
db = SQLAlchemy (app)

from shop.admin import routes