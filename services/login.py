from flask import Blueprint, request, make_response, session, abort
from werkzeug.security import check_password_hash

login_bp = Blueprint("Login Service", __name__)
db = None

@login_bp.route("/api/login", methods=["POST"])
def login():
    global db
    data = request.form
    email = data.get("email")
    password = data.get("password")
    
    cursor.execute("SELECT email, password FROM users WHERE email=%s;", (email,))
    result = cursor.fetchone()
    
    if result == None:
        abort(400)
    
    if email == result[0] and check_password_hash(result[1], password):
        session["email"] = email
        
        response = make_response("Authorized")
        response.status_code = 200
        return response
    
    response = make_response( "ERROR" )
    response.status_code = 401
    return response