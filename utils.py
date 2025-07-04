import jwt
from flask import request, jsonify
from config import JWT_SECRET
import bcrypt

def verify_token(token):
    return jwt.decode(token, JWT_SECRET, algorithms=["HS256"])

def hash_password(password):
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

def auth_required(f):
    def wrapper(*args, **kwargs):
        auth_header = request.headers.get('Authorization')
        if not auth_header or not auth_header.startswith("Bearer "):
            return jsonify({"error": "Missing or invalid token"}), 401
        try:
            token = auth_header.split()[1]
            decoded = verify_token(token)
            request.user = decoded
            return f(*args, **kwargs)
        except jwt.ExpiredSignatureError:
            return jsonify({"error": "Token expired"}), 401
        except jwt.InvalidTokenError:
            return jsonify({"error": "Invalid token"}), 401
    wrapper.__name__ = f.__name__
    return wrapper