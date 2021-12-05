import json

from initialize import app, db
from db_schema import User

from flask import request, make_response
from flask_bcrypt import Bcrypt
from flask_login import current_user


bcrypt = Bcrypt(app)


def token_required(f):
    @wraps(f)
    def decorated(*args,**kwargs):
        token=None

        if 'x-access-token' in request.headers:
            token=request.headers['x-access-token']

        if not token:
            return jsonify({'message':'token is missing!'}),401

        try:
            data=jwt.decode(token, app.config['SECRET_KEY'])
            current_user=mdl_user.query.filter_by(id=data['user_id']).first()
        except:
            return jsonify({'message':'token is invalid!'}),401

        return f(current_user,*args,**kwargs)
    return decorated


@app.route('/sign_up',methods=['POST'])
def sign_up():

        data = json.loads(request.values.get('json'))

        name = data['name']
        last_name = data['last_name']
        username = data['username']
        address = data['address']
        phone1 = data['phone1']
        phone2 = data['phone2']
        password = data['password']
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
    
    data = json.loads(request.values.get('json'))

    username = data['username']
    password = data['password']

    user = User.query.filter_by(username=username).first()
   
    if not user:
        return make_response('User not found', 400)

    if not bcrypt.check_password_hash(user.password, password):
        return make_response('Invalid credentials', 401)
    
    return make_response('User correctly logged in', 200)