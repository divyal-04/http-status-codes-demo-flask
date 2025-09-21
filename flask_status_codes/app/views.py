from flask import request, jsonify, redirect, url_for, abort
import time
from functools import wraps

fake_db = {
    "users": {
        1: {"name": "Divyal", "role": "admin"},
        2: {"name": "Test", "role": "viewer"}
    }
}

# 200 OK
def get_user():
    user_id = request.args.get('id', type=int)
    if user_id and user_id in fake_db["users"]:
        return jsonify(fake_db["users"][user_id]), 200
    return jsonify({"error": "User not found"}), 404

# 201 Created
def create_user():
    data = request.get_json()
    if data and "name" in data:
        return jsonify({"message": "User created"}), 201
    return jsonify({"error": "Missing name field"}), 400

# 204 No Content
def delete_user():
    user_id = request.args.get('id', type=int)
    if user_id in fake_db["users"]:
        del fake_db["users"][user_id]
        return '', 204
    return jsonify({"error": "User not found"}), 404

# 301 Moved Permanently
def old_route():
    return redirect(url_for('new_route'), code=301)

def new_route():
    return jsonify(message="You’ve been redirected"), 200

# 400 Bad Request
def bad_request():
    data = request.get_json()
    if not data:
        abort(400)
    return jsonify(message="Data received"), 200

# 401 Unauthorized
def protected_route():
    auth = request.headers.get("Authorization")
    if auth != "demo_token":
        abort(401)
    return jsonify(message="Authorized access")

# 403 Forbidden
def forbidden_route():
    user_id = request.args.get('id', type=int)
    if fake_db["users"].get(user_id, {}).get("role") != "admin":
        abort(403)
    return jsonify(message="Access granted")

# 405 Method Not Allowed
def method_not_allowed():
    if request.method != "POST":
        abort(405)
    return jsonify(message="Valid POST request")

# 408 Request Timeout
def delayed_response():
    delay = request.args.get('delay', default=5, type=int)

    time.sleep(delay) 
    return jsonify(message=f"Response delayed by {delay} seconds"), 200

# 429 Too Many Requests
rate_limit_count = 0
def rate_limited():
    global rate_limit_count
    rate_limit_count += 1
    if rate_limit_count > 3:
        abort(429)
    return jsonify(message="You're within the limit")

# 500 Internal Server Error
def cause_error():
    return 1 / 0 
