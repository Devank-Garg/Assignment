from flask import Flask, jsonify
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

# Store Data Endpoint
@app.route('/users', methods=['POST'])
def add_user():
    sample_data = {"name": "John Doe", "email": "john.doe@example.com"}
    user_id = db.insert_one(sample_data).inserted_id
    return jsonify({"message": "User added successfully", "user_id": str(user_id)})

# Retrieve Data Endpoint
@app.route('/users', methods=['GET'])
def get_users():
    users = list(db.find({}, {"_id": 0}))  # Excluding MongoDB _id for simplicity
    return jsonify({"users": users})

if __name__ == '__main__':
    app.run(debug=True)