from flask import jsonify, request
from flask_jwt_extended import create_access_token, jwt_required
from werkzeug.security import check_password_hash, generate_password_hash

# Mock user data
users = {'admin': generate_password_hash('password'),
         'khoa': generate_password_hash('449backend')}

def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if username not in users or not check_password_hash(users[username], password):
        return jsonify({'message': 'Invalid credentials'}), 401

    access_token = create_access_token(identity=username)
    return jsonify({'access_token': access_token}), 200

@jwt_required()
def protected_endpoint():
    return jsonify({'message': 'You are authorized'}), 200
