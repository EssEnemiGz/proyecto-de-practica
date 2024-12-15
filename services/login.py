from flask import Blueprint, request, make_response, session

login_bp = Blueprint("Login Service", __name__)

@login_bp.route("/api/login", methods=["POST"])
def login():
    data = request.form
    email = data.get("email")
    password = data.get("password")
    
    if email == "biscenp@gmail.com" and password == "12345":
        session["user_email"] = email
        
        response = make_response("Authorized")
        response.status_code = 200
        return response
    
    response = make_response( "ERROR" )
    response.status_code = 401
    return response