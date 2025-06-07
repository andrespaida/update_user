from flask import Blueprint, request, jsonify
from db import get_db_connection
from models import update_user
from utils import auth_required, hash_password

routes = Blueprint('routes', __name__)

@routes.route('/users/<int:user_id>', methods=['PUT'])
@auth_required
def update_user_route(user_id):
    requester = request.user
    data = request.get_json()
    allowed_fields = ['name', 'email', 'password', 'role']

    # Solo el usuario puede editarse a sí mismo, excepto admin
    if requester['role'] != 'admin' and requester['id'] != user_id:
        return jsonify({"error": "You can only update your own profile"}), 403

    fields = {}
    for key in allowed_fields:
        if key in data:
            if key == 'role' and requester['role'] != 'admin':
                return jsonify({"error": "Only admins can change roles"}), 403
            elif key == 'password':
                fields[key] = hash_password(data[key])
            else:
                fields[key] = data[key]

    if not fields:
        return jsonify({"error": "No valid fields to update"}), 400

    try:
        conn = get_db_connection()
        update_user(conn, user_id, fields)
        conn.close()
        return jsonify({"message": "User updated successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
