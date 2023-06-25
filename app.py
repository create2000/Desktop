from flask import Flask, request, jsonify
from flask_cors import CORS
# from dotenv import load_dotenv
# load_dotenv()
from secrets import token_hex
from database import db
from os import getenv

app = Flask(__name__)
CORS(app, resources={r'/*': {'origins': '*'}})

user_collection = db['user']

class User:
    def __init__(self, first_name, last_name, email, password):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password

@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    first_name = data['first_name']
    last_name = data['last_name']
    email = data['email']
    password = data['password']

new_user = User(first_name='Anthony', last_name='Onah', email='onah@gmail.com', password='secret')

result = user_collection.insert_one(new_user.__dict__)

if result.inserted_id:
    return jsonify(message='User registered successfully'), 200
else:
    return jsonify(message='Failed to register user'), 500

if __name__ == '__main__':
    app.run(debug=True)
    

app.config['secret_key'] = getenv('SECRET_KEY')

if __name__ == '__main__':
    app.run(debug = getenv("ENVIRONMENT") == 'development')