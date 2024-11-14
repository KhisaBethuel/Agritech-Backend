from flask import Blueprint,request,make_response
from models import *
from flask_jwt_extended import jwt_required


message_blueprint = Blueprint("message_blueprint", __name__)


# CRUD Operations for Messages
@message_blueprint.route('/messages', methods=['GET'])
def messages():
    messages = [message.to_dict() for message in Message.query.all()]
    return make_response(jsonify(messages), 200)
    
    
@message_blueprint.route('/messages', methods=['POST'])
@jwt_required()
def message():
    try:
        new_message = Message(
            content=request.json.get("content"),
            sender_id=request.json.get("sender_id"),
            recipient_id=request.json.get("recipient_id")
        )
        db.session.add(new_message)
        db.session.commit()
        return make_response(new_message.to_dict(), 201)
    except Exception as e:
        return make_response({"errors": ["Failed to create message"]}, 400)

@message_blueprint.route('/messages/<int:message_id>', methods=['GET', 'PUT', 'DELETE'])
@jwt_required()
def message(message_id):
    message = Message.query.get(message_id)
    if not message:
        return make_response({"error": "Message not found"}, 404)

    if request.method == 'GET':
        return make_response(message.to_dict(), 200)

    elif request.method == 'PUT':
        data = request.get_json()
        message.content = data.get("content", message.content)
        db.session.commit()
        return make_response(message.to_dict(), 200)

    elif request.method == 'DELETE':
        db.session.delete(message)
        db.session.commit()
        return make_response({"message": "Message deleted successfully"}, 204)

