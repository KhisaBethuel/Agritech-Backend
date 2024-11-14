from flask import Blueprint,request,make_response
from models import *
from flask_jwt_extended import jwt_required

likes_bp = Blueprint("likes_bp", __name__)

# CRUD Operations for Likes
@likes_bp.route('/likes', methods=['POST'])
@jwt_required()
def create_like():
    try:
        new_like = Like(
            user_id=request.json.get("user_id"),
            post_id=request.json.get("post_id")
        )
        db.session.add(new_like)
        db.session.commit()
        return make_response(new_like.to_dict(), 201)
    except Exception as e:
        return make_response({"errors": ["Failed to create like"]}, 400)

@likes_bp.route('/likes/<int:like_id>', methods=['DELETE'])
@jwt_required()
def delete_like(like_id):
    like = Like.query.get(like_id)
    if not like:
        return make_response({"error": "Like not found"}, 404)

    db.session.delete(like)
    db.session.commit()
    return make_response({"message": "Like deleted successfully"}, 204)