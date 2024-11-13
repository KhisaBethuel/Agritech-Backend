from flask import Blueprint,request,make_response

auth_blueprint = Blueprint("auth_blueprint", __name__)

@auth_blueprint.route("/auth")
def auth():
    return {"message": "auth is working"}


# 1. Signup Route
@app.route('/signup', methods=['POST'])
def signup():
    try:
        # Create a new user
        new_user = Signup(
            username=request.json.get("username"),
            password=request.json.get("password")
        )

        db.session.add(new_user)
        db.session.commit()

        # Generate JWT tokens
        access_token = create_access_token(identity=new_user.id)
        refresh_token = create_refresh_token(identity=new_user.id)

        response_body = {
            "user": new_user.to_dict(),
            "access_token": access_token,
            "refresh_token": refresh_token
        }
        return make_response(response_body, 201)

    except Exception as e:
        print(e)  # Logging for debugging
        return make_response({"errors": ["Signup failed"]}, 400)

# 2. Login Route
@app.route('/login', methods=['POST'])
def login():
    try:
        # Authenticate user
        user = Login.query.filter_by(username=request.json.get("username")).first()
        if user and user.check_password(request.json.get("password")):
            access_token = create_access_token(identity=user.id)
            refresh_token = create_refresh_token(identity=user.id)

            response_body = {
                "user": user.to_dict(),
                "access_token": access_token,
                "refresh_token": refresh_token
            }
            return make_response(response_body, 200)

        return make_response({"errors": ["Invalid credentials"]}, 401)

    except Exception as e:
        print(e)  # Logging for debugging
        return make_response({"errors": ["Login failed"]}, 400)