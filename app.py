from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory database
users = {
    "1": {"name": "John", "email": "john@example.com"},
    "2": {"name": "Jane", "email": "jane@example.com"}
}

@app.route('/')
def home():
    return """
    <h1>User Management API</h1>
    <p>Endpoints:</p>
    <ul>
        <li>GET /users - List all users</li>
        <li>GET /users/1 - Get specific user</li>
        <li>POST /users - Create new user (use Postman/curl)</li>
    </ul>
    """

@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users)

@app.route('/users/<user_id>', methods=['GET'])
def get_user(user_id):
    if user_id in users:
        return jsonify(users[user_id])
    return jsonify({"error": "User not found"}), 404

@app.route('/users', methods=['POST'])
def add_user():
    new_user = request.get_json()
    if not new_user or 'name' not in new_user or 'email' not in new_user:
        return jsonify({"error": "Bad request"}), 400
    
    new_id = str(len(users) + 1)
    users[new_id] = new_user
    return jsonify({"id": new_id}), 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
