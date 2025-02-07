from flask import Flask, jsonify, request
from flask_pymongo import PyMongo

app = Flask(__name__)

# MongoDB Configuration
app.config["MONGO_URI"] = "mongodb://localhost:27017/userdb"
mongo = PyMongo(app)

db = mongo.db.users  # Collection in MongoDB

# Welcome Endpoint
@app.route('/', methods=['GET'])
def welcome():
    return jsonify({"message": "Welcome to the Flask REST API!"})

# Store Sample Data Endpoint
@app.route('/add_sample_user', methods=['POST'])
def add_sample_user():
    sample_data = {"name": "John Doe", "email": "john.doe@example.com"}
    user_id = db.insert_one(sample_data).inserted_id
    return jsonify({"message": "User added successfully", "user_id": str(user_id)})

# Store User Data from Request Endpoint
@app.route('/add_user', methods=['POST'])
def add_user():
    data = request.get_json()
    if not data or "name" not in data or "email" not in data:
        return jsonify({"error": "Invalid input data"}), 400
    user_id = db.insert_one(data).inserted_id
    return jsonify({"message": "User added successfully", "user_id": str(user_id)})

# Retrieve Data Endpoint
@app.route('/get_users', methods=['GET'])
def get_users():
    users = list(db.find({}, {"_id": 0}))  # Excluding MongoDB _id for simplicity
    return jsonify({"users": users})

if __name__ == '__main__':
    app.run(debug=True)
