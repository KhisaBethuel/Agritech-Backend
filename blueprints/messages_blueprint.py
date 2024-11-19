from flask import Blueprint,request,make_response,jsonify
from models import *
from flask_jwt_extended import jwt_required, get_jwt_identity


message_blueprint = Blueprint("message_blueprint", __name__)


# CRUD Operations for Messages
@message_blueprint.route('/messages', methods=['GET'])
def messages():
    messages = [message.to_dict() for message in Message.query.all()]
    return make_response(jsonify(messages), 200)
    
    
@message_blueprint.route('/message', methods=['POST'])
@jwt_required()
def post_message():
    try:
        sender_id = get_jwt_identity()
        recipient_id = request.json.get("recipient_id")
        content = request.json.get("content")

        if not content or not content.strip():
            return make_response({"error": "Message content cannot be empty"}, 400)

        sender = User.query.get(sender_id)
        recipient = User.query.get(recipient_id)

        if not sender:
            return make_response({"error": "Invalid sender"}, 404)
        recipient_expert = Expert.query.get(recipient_id)

        if not recipient_expert:
            return make_response({"error": "Recipient is not an expert or does not exist"}, 404)

        new_message = Message(
            content=content,
            sender_id=sender_id,
            recipient_id=recipient_id
        )
        db.session.add(new_message)
        db.session.commit()

        return make_response(new_message.to_dict(), 201)
    except Exception as e:
        return make_response({"errors": ["Failed to create message", str(e)]}, 400)

@message_blueprint.route('/messages/inbox', methods=['GET'])
@jwt_required()
def get_inbox():
    try:
        user_id = get_jwt_identity()
        messages = Message.query.filter_by(recipient_id=user_id).all()
        if not messages:
            return make_response({"error": "No messages found"}, 404)

        messages_list = [message.to_dict() for message in messages]
        return make_response(jsonify(messages_list), 200)
    except Exception as e:
        return make_response({"errors": ["Failed to fetch inbox messages", str(e)]}, 400)

@message_blueprint.route('/messages/sent', methods=['GET'])
@jwt_required()
def get_outbox():
    try:
        user_id = get_jwt_identity()
        messages = Message.query.filter_by(sender_id=user_id).all()

        messages_list = [message.to_dict() for message in messages]
        if not messages_list:
            return make_response({"message": "No sent messages found"}, 404)

        return make_response(jsonify(messages_list), 200)
    except Exception as e:
        return make_response({"errors": ["Failed to fetch sent messages", str(e)]}, 400)


@message_blueprint.route('/messages/conversation/<int:user_id>', methods=['GET'])
@jwt_required()
def get_conversation(user_id):
    try:
        current_user_id = get_jwt_identity()

        messages = Message.query.filter(
            (Message.sender_id == current_user_id) & (Message.recipient_id == user_id) |
            (Message.sender_id == user_id) & (Message.recipient_id == current_user_id)
        ).order_by(Message.created_at).all()

        if not messages:
            return make_response({"error": "No messages found in the conversation"}, 404)

        messages_list = [message.to_dict() for message in messages]
        return make_response(jsonify(messages_list), 200)
    except Exception as e:
        return make_response({"errors": ["Failed to fetch conversation", str(e)]}, 400)

