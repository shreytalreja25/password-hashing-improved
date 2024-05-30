from flask import Flask, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

# Mock function to simulate database retrieval
def get_stored_hashed_password_from_db():
    # This should be replaced with actual database retrieval
    return "stored_hashed_password"

@app.route('/register', methods=['POST'])
def register():
    password = request.form.get('password')
    if not password:
        return jsonify({"error": "Password is required"}), 400
    
    # Since the password is already hashed once on the client-side, we re-hash it for storage
    double_hashed_password = generate_password_hash(password)
    
    # Store double_hashed_password in the database (mocked here)
    # In a real application, you would store this in a database
    print(f"Storing hashed password: {double_hashed_password}")

    return jsonify({"message": "User registered successfully"}), 201

@app.route('/login', methods=['POST'])
def login():
    password = request.form.get('password')
    stored_double_hashed_password = get_stored_hashed_password_from_db()  # Retrieve from database

    if check_password_hash(stored_double_hashed_password, password):
        return jsonify({"message": "Login successful"}), 200
    else:
        return jsonify({"error": "Invalid credentials"}), 401

if __name__ == '__main__':
    app.run(debug=True)
