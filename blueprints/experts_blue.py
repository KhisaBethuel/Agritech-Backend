from flask import Blueprint,request,make_response,jsonify
from models import *
from flask_jwt_extended import jwt_required, get_jwt_identity

expert_blueprint = Blueprint("experts_blueprint", __name__)

# CRUD Operations for Experts
@expert_blueprint.route('/experts', methods=['GET'])
def get_experts():
    try:
        experts = [expert.to_dict() for expert in Expert.query.all()]
        if not experts:
            return make_response({"message": "No experts found"}, 404)
        return make_response(jsonify(experts), 200)
    except Exception as e:
        return make_response({"errors": [str(e)]}, 500)

@expert_blueprint.route('/experts', methods=['POST'])
@jwt_required()
def create_expert():
    current_user_id = get_jwt_identity()

    try:
        username = request.json.get("username")
        expertise_field = request.json.get("expertise_field")
        profile_image = request.json.get("profile_image", None)
        user_id = current_user_id 

        if not username or not expertise_field:
            return make_response(
                {"errors": ["Missing required fields: username or expertise_field"]}, 400
            )

        new_expert = Expert(
            username=username,
            expertise_field=expertise_field,
            profile_image=profile_image,
            user_id=user_id,
        )
        db.session.add(new_expert)
        db.session.commit()

        return make_response(new_expert.to_dict(), 201)
    except Exception as e:
        return make_response({"errors": [str(e)]}, 400)


@expert_blueprint.route('/experts/<int:expert_id>', methods=['GET', 'PUT', 'DELETE'])
@jwt_required()
def expert(expert_id):
    expert = Expert.query.get(expert_id)
    if not expert:
        return make_response({"error": "Expert not found"}, 404)

    current_user_id = get_jwt_identity()
    if expert.user_id != current_user_id:
        return make_response({"error": "You do not have permission to modify this expert."}, 403)

    if request.method == 'GET':
        return make_response(expert.to_dict(), 200)
    
    elif request.method == 'PUT':
        data = request.get_json()
        expert.username = data.get("username", expert.username)
        expert.expertise_field = data.get("expertise_field", expert.expertise_field)
        expert.profile_image = data.get("profile_image", expert.profile_image)

        db.session.commit()

        return make_response(expert.to_dict(), 200)

    elif request.method == 'DELETE':
        db.session.delete(expert)
        db.session.commit()
        return make_response({"message": "Expert deleted successfully"}, 204)