from flask import Blueprint,request,make_response,jsonify
from models import *
from flask_jwt_extended import jwt_required, get_jwt_identity

comments_bp = Blueprint("comments_bp", __name__)



# CRUD Operations for Comments
@comments_bp.route('/comments', methods=['POST'])
@jwt_required()
def post_comment():
    user_id = get_jwt_identity()  


    content = request.json.get('content')
    post_id = request.json.get('post_id')

    if not content or not post_id:
        return make_response({"error": "Content and post_id are required"}, 400)

    try:
        new_comment = Comment(
            content=content,
            user_id=user_id,  
            post_id=post_id
        )
        db.session.add(new_comment)
        db.session.commit()
        return make_response(new_comment.to_dict(), 201)
    except Exception as e:
        return make_response({"errors": ["Failed to create comment", str(e)]}, 400)


@comments_bp.route('/comments/<int:post_id>', methods=['GET'])
def get_comments_for_post(post_id):
    comments = Comment.query.filter_by(post_id=post_id).all()
    if not comments:
        return make_response({"error": "No comments found for this post"}, 404)

    comments_list = [comment.to_dict() for comment in comments]
    return make_response(jsonify(comments_list), 200)


@comments_bp.route('/comments/<int:comment_id>', methods=['PUT', 'DELETE'])
@jwt_required()
def update_or_delete_comment(comment_id):
    comment = Comment.query.get(comment_id)

    if not comment:
        return make_response({"error": "Comment not found"}, 404)

    user_id = get_jwt_identity()

    if comment.user_id != user_id:
        return make_response({"error": "You are not authorized to modify this comment"}, 403)

    if request.method == 'PUT':
        content = request.json.get('content')

        if not content:
            return make_response({"error": "Content is required to update the comment"}, 400)

        try:
            comment.content = content
            db.session.commit()
            return make_response(comment.to_dict(), 200)
        except Exception as e:
            return make_response({"errors": ["Failed to update comment", str(e)]}, 400)

    elif request.method == 'DELETE':
        try:
            db.session.delete(comment)
            db.session.commit()
            return make_response({"message": "Comment deleted successfully"}, 204)
        except Exception as e:
            return make_response({"errors": ["Failed to delete comment", str(e)]}, 400)
