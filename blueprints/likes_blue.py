from flask import Blueprint,request,make_response,jsonify
from models import *
from flask_jwt_extended import jwt_required, get_jwt_identity

likes_bp = Blueprint("likes_bp", __name__)

# CRUD Operations for Likes
@likes_bp.route('/likes', methods=['POST'])
@jwt_required()
def create_like():
    try:
        user_id = get_jwt_identity()

        post_id = request.json.get("post_id")
        if not post_id:
            return make_response({"error": "Post ID is required"}, 400)

        existing_like = Like.query.filter_by(user_id=user_id, post_id=post_id).first()
        if existing_like:
            return make_response({"error": "User already liked this post"}, 400)

        new_like = Like(user_id=user_id, post_id=post_id)
        db.session.add(new_like)
        db.session.commit()

        return make_response(new_like.to_dict(), 201)
    except Exception as e:
        return make_response({"errors": [f"Failed to create like: {str(e)}"]}, 400)


@likes_bp.route('/likes/<int:like_id>', methods=['DELETE'])
@jwt_required()
def delete_like(like_id):
    like = Like.query.get(like_id)
    if not like:
        return make_response({"error": "Like not found"}, 404)

    user_id = get_jwt_identity()
    if like.user_id != user_id:
        return make_response({"error": "You can only delete your own likes"}, 403)

    db.session.delete(like)
    db.session.commit()
    return make_response({"message": "Like deleted successfully"}, 204)


@likes_bp.route('/likes/post/<int:post_id>', methods=['GET'])
def get_likes_for_post(post_id):
    post = Blog.query.get(post_id)
    if not post:
        return make_response({"error": "Post not found"}, 404)

    likes = [like.to_dict() for like in post.likes]
    return make_response(jsonify(likes), 200)
