from flask import Blueprint,request,make_response
from models import *

expert_blueprint = Blueprint("experts_blueprint", __name__)

# CRUD Operations for Experts
@expert_blueprint.route('/experts', methods=['GET', 'POST'])
def experts():
    if request.method == 'POST':
        try:
            new_expert = Expert(
                name=request.json.get("name"),
                field=request.json.get("field")
            )
            db.session.add(new_expert)
            db.session.commit()
            return make_response(new_expert.to_dict(), 201)
        except Exception as e:
            return make_response({"errors": ["Failed to create expert"]}, 400)

    elif request.method == 'GET':
        try:
            experts = {expert.to_dict() for expert in Expert.query.all()}
            if experts is None:
                return make_response({"message" : "No expert"})
            else:
                return make_response(jsonify(experts), 200)
        except Exception as e:
            return make_response({"message" : "No expert"}, )
        

@expert_blueprint.route('/experts/<int:expert_id>', methods=['GET', 'PUT', 'DELETE'])
def expert(expert_id):
    expert = Expert.query.get(expert_id)
    if not expert:
        return make_response({"error": "Expert not found"}, 404)

    if request.method == 'GET':
        return make_response(expert.to_dict(), 200)
    
    elif request.method == 'PUT':
        data = request.get_json()
        expert.name = data.get("name", expert.name)
        expert.field = data.get("field", expert.field)
        db.session.commit()
        return make_response(expert.to_dict(), 200)

    elif request.method == 'DELETE':
        db.session.delete(expert)
        db.session.commit()
        return make_response({"message": "Expert deleted successfully"}, 204)

