import os
from flask import Flask, jsonify, request
from flask_jwt_extended import JWTManager, create_access_token, jwt_required
from pymongo import MongoClient
from dotenv import load_dotenv
from flask_cors import CORS  # Added this to match your error log requirements

load_dotenv()

app = Flask(__name__)
CORS(app)  # Initialize CORS to allow frontend requests
app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY', 'default-secret-key')
jwt = JWTManager(app)

# MongoDB Connection
# Use a default string for local testing, but GitHub will use the Secret
MONGO_URI = os.getenv('MONGO_URI', 'mongodb://localhost:27017/')
client = MongoClient(MONGO_URI)
db = client['exp10_db']

@app.route('/')
def home():
    return jsonify({"message": "CI/CD Pipeline is Working!"})

@app.route('/api/signup', methods=['POST'])
def signup():
    data = request.get_json()
    if not data or 'email' not in data:
        return jsonify({"error": "Missing email"}), 400
    return jsonify({"message": "User created"}), 201

@app.route('/api/protected')
@jwt_required()
def protected():
    return jsonify({"message": "Access granted"})

if __name__ == '__main__':
    app.run(debug=True)