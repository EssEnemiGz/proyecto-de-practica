from flask import Blueprint, request, make_response, session, abort
from werkzeug.security import generate_password_hash

register_bp = Blueprint("Register Service", __name__)
db, cursor = None, None

@register_bp.route("/api/register", methods=["POST"])
def register():
    global db, cursor
    data = request.form
    email = data.get("email")
    password = data.get("password")
    if email == "" or password == "":
        abort(400)
    
    try:
        password_hashed = generate_password_hash(password)
        cursor.execute("INSERT INTO users(email, password) VALUES(%s, %s);", (email, password_hashed) )
        db.commit()
        session['email'] = email
    except:
        print("FALLO LA CONSULTA SQL")
        abort(500)
    
    response = make_response( "DONE" )
    response.status_code = 200
    return response