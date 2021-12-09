import jwt
from datetime import datetime, timedelta


def generate_token(app, user_id):

    payload = {
        'exp':datetime.utcnow() + timedelta(days=60),
        'iat':datetime.utcnow(),
        'sub':str(user_id)
    }
    
    token = jwt.encode(payload, app.config['SECRET_KEY'], algorithm='HS256')

    return token