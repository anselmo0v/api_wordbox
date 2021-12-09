import json
import requests
from api_wordbox import __version__


def test_version():
    assert __version__ == '0.1.0'

def test_signup():
    data={
        'password':'pass_prueba',
        'name':'Prueba',
        'last_name':'prueba',
        'username':'prueba',
        'address':'carrera 8 # 2 - 12',
        'phone1':'123456',
        'phone2':'654321'
    }
    response = requests.post('http://127.0.0.1:5000/sign_up', data=data)
    assert json.loads(response.content)['Success'] == 'User has been signed up'

def test_login():

    data={
        'username':'prueba',
        'password':'pass_prueba'
    }
    response = requests.post('http://127.0.0.1:5000/login', data=data)
    assert response.content == 'User correctly logged in'