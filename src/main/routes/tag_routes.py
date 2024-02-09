from flask import Blueprint, request, jsonify

tags_routs_bp = Blueprint('tags_routes', __name__)

@tags_routs_bp.route('/create_tag', methods=['POST'])

def create_tags():
    print(request.json)
    return jsonify({'resp':'ok'}), 200
