import email
import json
import jwt
from functools import wraps
from flask import Flask, jsonify, request, make_response,Response
from flask_restful import Resource, Api
from flask_cors import CORS
import flask_sqlalchemy
import requests
from flask_sqlalchemy import SQLAlchemy

from faunadb import query as q
from faunadb.objects import Ref
from faunadb.client import FaunaClient
import datetime

app = Flask(__name__)
api = Api(app)
cors = CORS(app)
db = SQLAlchemy(app)

app.config['SECRET_KEY'] = "djwedwuehdhdwdhwdhwdh"


def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        req = request.get_json()
        token = req["token"]
        if not token:
            message = json.dumps({'message':'Token is missing'})
            return Response(message, status=403, mimetype='application/json')
        try:
            data = jwt.decode(token, "secret", algorithms=["HS256"])
            response = json.dumps({'message':'Valid token'})
            return Response(response, status=200, mimetype='application/json')
        except:
            res = json.dumps({'message':'No token to make a request'})
            return Response(res, status=403, mimetype='application/json')
        return f(*args, **kwargs)
    return decorated
    






class Login(Resource):
    def get(self):
        return {'GET': 'This is a get request'}

    def post(self):
        r = request.get_json()
        print(r)
        Email = r["Email"]
        password = r["Pword"]
        mail = User.query.filter_by(email=Email).first()
        passw = User.query.filter_by(password=password).first()
        key ="secret"
        if mail and passw:
            tokenval = jwt.encode({'user':Email}, key, algorithm="HS256").decode('utf-8')
            token = str(tokenval)
            print(type(tokenval))
            print(tokenval)
            response = {"res":"Valid email and password", 'token':token}
            return {"res":"Valid email and password", 'token':token}
        else:
            response = json.dumps({"res":"Invalid email or Password"})
            return Response(response, status=403, mimetype='application/json')
        
    
class user(Resource):
    
    def post(self):
        req = request.get_json()
        token = req["token"]
        
        if not token:
            message = json.dumps({'message':'Token is missing'})
            return Response(message, status=403, mimetype='application/json')
        try:
            data = jwt.decode(token, "secret", algorithms=["HS256"])
            response = json.dumps({'message':'Valid token','user':data})
            return Response(response, status=200, mimetype='application/json')
        except Exception as e:
            print(e)
            res = json.dumps({'message':'No token to make a request'})
            return Response(res, status=403, mimetype='application/json')
        
        



api.add_resource(Login, '/api/login')
api.add_resource(user,'/api/me/user')


if __name__ == '__main__':
    app.run(debug=True)