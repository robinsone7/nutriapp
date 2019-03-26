# services/users/project/__init__.py
import os

from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

# instaciamos la app
app = Flask(__name__)

#estableciendo configuracion
#app.config.from_object('project.config.DevelopmentConfig')
app_settings = os.getenv('APP_SETTINGS')
app.config.from_object(app_settings)

db= SQLAlchemy(app)

class Use(db.Model):
    __tablename__='users'
    id=db.Column(db.Integer, primary_key=True, autoincremente=True)
    username=db.Column(db.String(128), nullabel=False)    
    email=db.Column(db.String(128), nullabel=False)
    active=db.Column(db.Boolean(), default=True, nullabel=False)

    def __init__(self, username, email)
        self.username = username
        self.email = email
    

@app.route('/users/ping',methods=['GET'])
def ping_pong():
    return jsonify({
        'status':'success',
        'message':'pong'
    })

