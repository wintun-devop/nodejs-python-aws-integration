from flask import Blueprint,jsonify,make_response,request
#import api prefix
from server.server_config import AUTH_API_LINK

#import bcrypt from server __init__ module
from server import bcrypt
#import database and model from models
from server.models import db,Users

#register blue print
register_bp = Blueprint('register', __name__,url_prefix=AUTH_API_LINK)

@register_bp.route('/register',methods=["POST"])
def register_user():
    req_body = request.get_json()
    try:
        user_name = req_body['user_name']
        user_email = req_body['user_email']
        user_password = req_body['user_password']
        check_email_exist=Users.query.filter_by(email=user_email).first()
        print("check email exist",check_email_exist)
        if check_email_exist is not None:
            return make_response(jsonify({'status':'fail','msg':'already exist'}),400)
        hash_password = bcrypt.generate_password_hash(user_password).decode('utf-8')
        # print(hash_password)
        new_user = Users(name=user_name,email=user_email,password=hash_password)
        db.session.add(new_user)
        db.session.commit()
        user=Users.query.filter_by(email=user_email).first()
        response={"id":user.id,"name":user.name,"email":user.email,"createdAt":user.createdAt}
        return make_response(jsonify(response),201)
    except:
        return make_response(jsonify({"status":"failed","msg":"Internal Server Error"}),500)
        
    
    
    