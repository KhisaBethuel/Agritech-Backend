from flask import Blueprint,request,make_response
from models import *
from flask_jwt_extended import jwt_required

blogs_bp = Blueprint("blogs_bp", __name__)

# 3. CRUD Operations for Blogs
@blogs_bp.route('/blogs', methods=['GET', 'POST'])
@jwt_required()
def blogs():
    if request.method == 'POST':
        try:
            new_blog = Blog(
                title=request.json.get("title"),
                image=request.json.get("image")
                content=request.json.get("content")  
            )
            db.session.add(new_blog)
            db.session.commit()

            response_body = new_blog.to_dict()
            return make_response(response_body, 201)
        except Exception as e:
            print(e)  # Logging for debugging
            return make_response({"errors": ["Failed to create blog"]}, 400)

    elif request.method == 'GET':
        blogs = {blog.to_dict() for blog in Blog.query.all()}
        return make_response(jsonify(blogs), 200)

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
            blog.image = data.get("image",blog.image)
            blog.content = data.get("content", blog.content)
            db.session.commit()
            return make_response(blog.to_dict(), 200)
        except Exception as e:
            print(e)  
            return make_response({"errors": ["Failed to update blog"]}, 400)

    elif request.method == 'DELETE':
        try:
            db.session.delete(blog)
            db.session.commit()
            return make_response({"message": "Blog deleted successfully"}, 204)
        except Exception as e:
            print(e)  
            return make_response({"errors": ["Failed to delete blog"]}, 400)
