from flask import Blueprint,request,make_response
from models import *
from flask_jwt_extended import jwt_required

comments_bp = Blueprint("comments_bp", __name__)



# CRUD Operations for Comments
@comments_bp.route('/comments', methods=['GET', 'POST'])
@jwt_required()
def comments():
    if request.method == 'POST':
        try:
            new_comment = Comment(
                content=request.json.get("content"),
                user_id=request.json.get("user_id"),
                post_id=request.json.get("post_id")
            )
            db.session.add(new_comment)
            db.session.commit()
            return make_response(new_comment.to_dict(), 201)
        except Exception as e:
            return make_response({"errors": ["Failed to create comment"]}, 400)

    elif request.method == 'GET':
        comments = {comment.to_dict() for comment in Comment.query.all()}
        return make_response(jsonify(comments), 200)

@comments_bp.route('/comments/<int:comment_id>', methods=['GET', 'PUT', 'DELETE'])
@jwt_required()
def comment(comment_id):
    comment = Comment.query.get(comment_id)
    if not comment:
        return make_response({"error": "Comment not found"}, 404)

    if request.method == 'GET':
        return make_response(comment.to_dict(), 200)

    elif request.method == 'PUT':
        data = request.get_json()
        comment.content = data.get("content", comment.content)
        db.session.commit()
        return make_response(comment.to_dict(), 200)

    elif request.method == 'DELETE':
        db.session.delete(comment)
        db.session.commit()
        return make_response({"message": "Comment deleted successfully"}, 204)