import requests
import jwt
import json
from functools import wraps


from .db_schema import User
from .initialize import app, db
from .tokens import generate_token

from flask_bcrypt import Bcrypt
from flask_login import current_user
from flask import request, make_response, jsonify


bcrypt = Bcrypt(app)


def token_required(f):
    @wraps(f)
    def decorated(*args,**kwargs):
        token = None

        if 'authorization' in request.headers:
            token = request.headers['authorization']

        if not token:
            return make_response(jsonify({'Error':'Token is missing!'}), 401)

        #try:
        data = jwt.decode(token, app.config['SECRET_KEY'], algorithms='HS256')
        current_user = User.query.filter_by(id=data['sub']).first()
        #except:
        #    return make_response(jsonify({'Error':'Token is invalid!'}), 401)

        return f(current_user,*args,**kwargs)
    return decorated


@app.route('/sign_up',methods=['POST'])
def sign_up():

        name = request.values.get('name')
        last_name = request.values.get('last_name')
        username = request.values.get('username')
        address = request.values.get('address')
        phone1 = request.values.get('phone1')
        phone2 = request.values.get('phone2')
        password = request.values.get('password')
        hashed_password=bcrypt.generate_password_hash(password).decode('utf-8')
        
        user=User(
            name=name,
            last_name=last_name,
            username=username,
            address=address,
            phone1=phone1,
            phone2=phone2,
            password_hash=hashed_password
        )
        db.session.add(user)
        db.session.commit()

        return {'Success':'User has been signed up'}



@app.route('/login',methods=['POST'])
def login():

    username = request.values.get('username')
    password = request.values.get('password')

    user = User.query.filter_by(username=username).first()
   
    if not user:
        return make_response('User not found', 400)

    if not bcrypt.check_password_hash(user.password_hash, password):
        return make_response('Invalid credentials', 401)

    user_id = User.query.with_entities(User.id).filter_by(username=username).first()[0]
    
    token = generate_token(app, user_id)


    return make_response(jsonify({'Success':'User correctly logged in', 'token':token}), 200)


@app.route('/check_token',methods=['GET'])
@token_required
def check_token(current_user):

    return make_response({'Success':'Token was correctly checked'})