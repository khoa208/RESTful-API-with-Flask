from flask import Flask, jsonify, request, send_from_directory
from flask_jwt_extended import JWTManager, create_access_token, jwt_required
from flask_mysqldb import MySQL
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)

# Configurations
app.config['SECRET_KEY'] = '449-midtern'
app.config['JWT_SECRET_KEY'] = 'jwtKhoaDo'
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'password'
app.config['MYSQL_DB'] = 'flask_rest_api'
app.config['UPLOAD_FOLDER'] = './uploads'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB limit

# Extensions
jwt = JWTManager(app)
mysql = MySQL(app)

# Ensure upload directory exists
if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])

# Import services
from services.auth_service import login, protected_endpoint
from services.file_service import upload_file
from services.public_service import public_route

# Register routes
app.route('/login', methods=['POST'])(login)
app.route('/protected', methods=['GET'])(protected_endpoint)
app.route('/upload', methods=['POST'])(upload_file)
app.route('/public', methods=['GET'])(public_route)

# Error handling
@app.errorhandler(400)
def bad_request(error):
    return jsonify({'message': 'Bad request', 'status': 400}), 400

@app.errorhandler(401)
def unauthorized(error):
    return jsonify({'message': 'Unauthorized access', 'status': 401}), 401

@app.errorhandler(404)
def not_found(error):
    return jsonify({'message': 'Resource not found', 'status': 404}), 404

@app.errorhandler(500)
def server_error(error):
    return jsonify({'message': 'Server error', 'status': 500}), 500

if __name__ == '__main__':
    app.run(debug=True)
