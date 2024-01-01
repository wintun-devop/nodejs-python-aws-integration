from flask import Blueprint,jsonify,make_response,request
from server.server_config import AUTH_API_LINK
from server import bcrypt
register_bp = Blueprint('register', __name__,url_prefix=AUTH_API_LINK)



@register_bp.route('/register',methods=["POST"])
def register_user():
    req_body = request.get_json()
    password = req_body['password']
    email = req_body['email']
    hash_password = bcrypt.generate_password_hash(password)
    print(hash_password)
    response={"email":email,"password":str(hash_password)}
    return make_response(jsonify(response),201)
    
    
    