from flask import Blueprint,request,make_response
from models import *

auth_blueprint = Blueprint("auth_blueprint", __name__)


# CRUD Operations for Communities
@app.route('/communities', methods=['GET', 'POST'])
def communities():
    if request.method == 'POST':
        try:
            new_community = Community(
                name=request.json.get("name"),
                description=request.json.get("description")
            )
            db.session.add(new_community)
            db.session.commit()
            return make_response(new_community.to_dict(), 201)
        except Exception as e:
            return make_response({"errors": ["Failed to create community"]}, 400)

    elif request.method == 'GET':
        communities = [community.to_dict() for community in Community.query.all()]
        return make_response(jsonify(communities), 200)

@app.route('/communities/<int:community_id>', methods=['GET', 'PUT', 'DELETE'])
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
        db.session.commit()
        return make_response(community.to_dict(), 200)

    elif request.method == 'DELETE':
        db.session.delete(community)
        db.session.commit()
        return make_response({"message": "Community deleted successfully"}, 204)