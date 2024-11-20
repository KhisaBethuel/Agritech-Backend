from flask import Blueprint,request,make_response
from flask_jwt_extended import create_access_token, create_refresh_token
from models import *
from flask_jwt_extended import jwt_required,get_jwt_identity
from sqlalchemy.exc import IntegrityError as SQLAlchemyIntegrityError




auth_blueprint = Blueprint("auth_blueprint", __name__)

@auth_blueprint.route('/signup', methods=['POST'])
def signup():
    try:
        username = request.json.get("username")
        email = request.json.get("email")
        password = request.json.get("password")

        if not username or not email or not password:
            return make_response({"errors": ["Username, email, and password are required"]}, 400)

        
        if User.query.filter((User.username == username) | (User.email == email)).first():
            return make_response({"errors": ["Username or email already exists"]}, 400)

        new_user = User(username=username, email=email)
        new_user.set_password(password)

        db.session.add(new_user)
        db.session.commit()

        response_body = {
            "message": "User created successfully"
        }
        return make_response(response_body, 201)

    except IntegrityError:
        db.session.rollback()
        return make_response({"errors": ["Username or email already exists"]}, 400)
    except Exception as e:
        return make_response({"errors": ["Signup failed", str(e)]}, 500)

# 2. Login Route
@auth_blueprint.route('/login', methods=['POST'])
def login():
    try:
        email = request.json.get('email')
        password = request.json.get('password')
        user = User.query.filter_by(email=email).first()
        if user and user.check_password(password):
            access_token = create_access_token(identity=user.id)
            refresh_token = create_refresh_token(identity=user.id)

            response_body = {
                "access token": access_token,
                "refresh token": refresh_token
            }
            return make_response(response_body, 200)

        return make_response({"errors": ["Invalid credentials"]}, 401)

    except Exception as e:
        print(e)
        return make_response({"errors": ["Login failed"]}, 400)

@auth_blueprint.route('/logout', methods=['POST'])
@jwt_required()
def logout():
    return make_response({"message": "Logout successful"}, 200)

@auth_blueprint.route('/profile/edit', methods=['PATCH'])
@jwt_required()
def edit_profile():
    try:
        current_user_id = get_jwt_identity()

        user = User.query.get(current_user_id)
        if not user:
            return make_response({"errors": ["User not found"]}, 404)

        username = request.json.get("username")
        email = request.json.get("email")
        bio = request.json.get("bio")
        profile_picture = request.json.get("profile_picture")

        if username:
            user.username = username
        if email:
            user.email = email
        if bio:
            user.bio = bio
        if profile_picture:
            user.profile_picture = profile_picture

        db.session.commit()

        response_body = {
            "message": "Profile updated successfully",
            "user": {
                "username": user.username,
                "email": user.email,
                "bio": user.bio,
                "profile_picture": user.profile_picture
            }
        }

        return make_response(response_body, 200)

    except Exception as e:
        print(e) 
        return make_response({"errors": ["Profile update failed", str(e)]}, 500)
    
    
@auth_blueprint.route('/follow_user', methods=['POST'])
@jwt_required()
def follow_user():
    try:
        current_user_id = get_jwt_identity()
        followed_user_id = request.json.get('followed_user_id')

        if current_user_id == followed_user_id:
            return make_response({"errors": ["You cannot follow yourself"]}, 400)

        existing_follow = UserFollow.query.filter_by(follower_id=current_user_id, followed_id=followed_user_id).first()
        if existing_follow:
            return make_response({"errors": ["You are already following this user"]}, 400)

        follow = UserFollow(follower_id=current_user_id, followed_id=followed_user_id)
        db.session.add(follow)
        db.session.commit()

        return make_response({"message": "Followed user successfully"}, 200)
    except Exception as e:
        db.session.rollback()
        return make_response({"errors": ["Failed to follow user", str(e)]}, 500)
    
    
@auth_blueprint.route('/unfollow_user', methods=['POST'])
@jwt_required()
def unfollow_user():
    try:
        current_user_id = get_jwt_identity()
        followed_user_id = request.json.get('followed_user_id')

        follow = UserFollow.query.filter_by(follower_id=current_user_id, followed_id=followed_user_id).first()
        if not follow:
            return make_response({"errors": ["You are not following this user"]}, 400)

        db.session.delete(follow)
        db.session.commit()

        return make_response({"message": "Unfollowed user successfully"}, 200)
    except Exception as e:
        db.session.rollback()
        return make_response({"errors": ["Failed to unfollow user", str(e)]}, 500)


@auth_blueprint.route('/follow_expert', methods=['POST'])
@jwt_required()
def follow_expert():
    try:
        current_user_id = get_jwt_identity()
        expert_id = request.json.get('expert_id')

        existing_follow = ExpertFollow.query.filter_by(user_id=current_user_id, expert_id=expert_id).first()
        if existing_follow:
            return make_response({"errors": ["You are already following this expert"]}, 400)

        follow = ExpertFollow(user_id=current_user_id, expert_id=expert_id)
        db.session.add(follow)
        db.session.commit()

        return make_response({"message": "Followed expert successfully"}, 200)
    except Exception as e:
        db.session.rollback()
        return make_response({"errors": ["Failed to follow expert", str(e)]}, 500)

@auth_blueprint.route('/unfollow_expert', methods=['POST'])
@jwt_required()
def unfollow_expert():
    try:
        current_user_id = get_jwt_identity()
        expert_id = request.json.get('expert_id')

        follow = ExpertFollow.query.filter_by(user_id=current_user_id, expert_id=expert_id).first()
        if not follow:
            return make_response({"errors": ["You are not following this expert"]}, 400)

        db.session.delete(follow)
        db.session.commit()

        return make_response({"message": "Unfollowed expert successfully"}, 200)
    except Exception as e:
        db.session.rollback()
        return make_response({"errors": ["Failed to unfollow expert", str(e)]}, 500)


@auth_blueprint.route('/followers_of_user/<int:user_id>', methods=['GET'])
@jwt_required()
def get_followers_of_user(user_id):
    try:
        followers = UserFollow.query.filter_by(followed_id=user_id).all()
        
        if not followers:
            return make_response({"message": "No followers found for this user"}, 404)

        follower_ids = [follower.follower_id for follower in followers]
        followers_data = User.query.filter(User.id.in_(follower_ids)).all()

        followers_list = [{"id": follower.id, "username": follower.username} for follower in followers_data]
        
        return make_response({"followers": followers_list}, 200)
    except Exception as e:
        return make_response({"errors": ["Failed to retrieve followers", str(e)]}, 500)


@auth_blueprint.route('/following_of_user/<int:user_id>', methods=['GET'])
@jwt_required()
def get_following_of_user(user_id):
    try:
        following = UserFollow.query.filter_by(follower_id=user_id).all()

        if not following:
            return make_response({"message": "This user is not following anyone"}, 404)

        followed_user_ids = [followed.followed_id for followed in following]
        followed_users = User.query.filter(User.id.in_(followed_user_ids)).all()

        following_list = [{"id": user.id, "username": user.username} for user in followed_users]
        
        return make_response({"following": following_list}, 200)
    except Exception as e:
        return make_response({"errors": ["Failed to retrieve following list", str(e)]}, 500)


@auth_blueprint.route('/followers_of_expert/<int:expert_id>', methods=['GET'])
@jwt_required()
def get_followers_of_expert(expert_id):
    try:
        followers = ExpertFollow.query.filter_by(expert_id=expert_id).all()

        if not followers:
            return make_response({"message": "No followers found for this expert"}, 404)

        follower_ids = [follower.user_id for follower in followers]
        followers_data = User.query.filter(User.id.in_(follower_ids)).all()

        followers_list = [{"id": follower.id, "username": follower.username} for follower in followers_data]

        return make_response({"followers": followers_list}, 200)
    except Exception as e:
        return make_response({"errors": ["Failed to retrieve expert followers", str(e)]}, 500)

@auth_blueprint.route('/following_of_expert_by_user/<int:user_id>', methods=['GET'])
@jwt_required()
def get_following_of_expert_by_user(user_id):
    try:
        following_experts = ExpertFollow.query.filter_by(user_id=user_id).all()

        if not following_experts:
            return make_response({"message": "This user is not following any expert"}, 404)

        expert_ids = [follow.expert_id for follow in following_experts]
        experts_data = Expert.query.filter(Expert.id.in_(expert_ids)).all()

        experts_list = [{"id": expert.id, "name": expert.name} for expert in experts_data]

        return make_response({"following_experts": experts_list}, 200)
    except Exception as e:
        return make_response({"errors": ["Failed to retrieve followed experts", str(e)]}, 500)


