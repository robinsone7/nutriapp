# services/users/project/__init__.py

from flask import Flask, jsonify

# instaciamos la app
app = Flask(__name__)

#estableciendo configuracion
app.config.from_object('project.config.DevelopmentConfig')

@app.route('/hola/mundo',methods=['GET'])
def real():
    return jsonify({
        'message':'hola'
    })

