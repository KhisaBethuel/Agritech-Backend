from flask import Blueprint,request,make_response, jsonify
from models import *
from flask_jwt_extended import jwt_required, get_jwt_identity

blogs_bp = Blueprint("blogs_bp", __name__)

# 3. CRUD Operations for Blog

from flask import request, jsonify, make_response

@blogs_bp.route('/blogs', methods=['GET'])
def get_blogs():
    
    page = request.args.get('page', 1, type=int)  
    per_page = request.args.get('per_page', 6, type=int)  

    blogs_query = Blog.query.paginate(page=page, per_page=per_page, error_out=False)

    
    blogs = [blog.to_dict() for blog in blogs_query.items]
    response = {
        'blogs': blogs,
        'total': blogs_query.total,  
        'page': blogs_query.page,    
        'per_page': blogs_query.per_page,  
        'pages': blogs_query.pages  
    }

    return make_response(jsonify(response), 200)


@blogs_bp.route('/blogs', methods=['POST'])
@jwt_required()
def create_blog():
    """
    Handles creating a new blog. Requires user authentication.
    """
    try:
        user_id = get_jwt_identity()
        if not user_id:
            return make_response({"errors": ["User not authenticated"]}, 401)

        new_blog = Blog(
            title=request.json.get("title"),
            image=request.json.get("image"),
            content=request.json.get("content"),
            user_id=user_id,
            created_at=datetime.utcnow()
        )

        db.session.add(new_blog)
        db.session.commit()

        response_body = new_blog.to_dict()
        return make_response(response_body, 201)

    except Exception as e:
        print(e)
        return make_response({"errors": ["Failed to create blog"]}, 400)
    
@blogs_bp.route('/blogs/<int:blog_id>', methods=['GET', 'PUT', 'DELETE'])
@jwt_required()
def blog(blog_id):
    blog = Blog.query.get(blog_id)
    if blog is None:
        return make_response({"error": "Blog not found"}, 404)

    if request.method == 'GET':
        return make_response(blog.to_dict(), 200)

    elif request.method == 'PUT':
        try:
            data = request.get_json()
            blog.title = data.get("title", blog.title)
            blog.image = data.get("image", blog.image)
            blog.content = data.get("content", blog.content)
            db.session.commit()
            return make_response(blog.to_dict(), 200)
        except Exception as e:
            print(f"Error: {str(e)}")
            return make_response({"errors": [str(e)]}, 400)

    elif request.method == 'DELETE':
        try:
            db.session.delete(blog)
            db.session.commit()
            return make_response({"message": "Blog deleted successfully"}, 204)
        except Exception as e:
            print(f"Error: {str(e)}")
            return make_response({"errors": [str(e)]}, 400)