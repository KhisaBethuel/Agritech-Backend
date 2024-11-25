from flask import Blueprint,request,make_response,jsonify
from models import *
from flask_jwt_extended import jwt_required, get_jwt_identity

communities_bp = Blueprint("communities_bp", __name__)


# CRUD Operations for Communities
@communities_bp.route('/communities', methods=['GET'])
def get_communities():
    communities = [community.to_dict() for community in Community.query.all()]
    return make_response(jsonify(communities), 200)

@communities_bp.route('/communities', methods=['POST'])
@jwt_required()
def create_community():
    try:
        user_id = get_jwt_identity()

        new_community = Community(
            name=request.json.get("name"),
            description=request.json.get("description"),
            user_id=user_id,
            image=request.json.get("image"), 
            category = request.json.get("category")
        )
        db.session.add(new_community)
        db.session.commit()

        return make_response(new_community.to_dict(), 201)

    except Exception as e:
        return make_response({"errors": ["Failed to create community", str(e)]}, 400)

@communities_bp.route('/communities/<int:community_id>', methods=['GET', 'PUT', 'DELETE'])
@jwt_required()
def community(community_id):
    community = Community.query.get(community_id)
    if not community:
        return make_response({"error": "Community not found"}, 404)

    if request.method == 'GET':
        return make_response(community.to_dict(), 200)

    elif request.method == 'PUT':
        data = request.get_json()
        community.name = data.get("name", community.name)
        community.description = data.get("description", community.description)
        community.image = data.get("image", community.image)
        db.session.commit()
        return make_response(community.to_dict(), 200)

    elif request.method == 'DELETE':
        db.session.delete(community)
        db.session.commit()
        return make_response({"message": "Community deleted successfully"}, 204)

    
    
@communities_bp.route('/communities/<int:community_id>/join', methods=['POST'])
@jwt_required()
def join_community(community_id):
    user_id = get_jwt_identity()

    community = Community.query.get(community_id)
    if not community:
        return make_response({"error": "Community not found"}, 404)

    existing_membership = UserCommunity.query.filter_by(user_id=user_id, community_id=community_id).first()
    if existing_membership:
        return make_response({"message": "You have already joined this community"}, 400)

    user_community = UserCommunity(user_id=user_id, community_id=community_id)
    db.session.add(user_community)
    db.session.commit()

    return make_response({"message": "You have successfully joined the community"}, 200)
