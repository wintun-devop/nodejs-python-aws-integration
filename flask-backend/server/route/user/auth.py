from flask import Blueprint,jsonify,make_response,request
#import api prefix
from server.server_config import AUTH_API_LINK

#import bcrypt from server __init__ module
from server import bcrypt
#import database and model from models
from server.models import db,Users

#import token services
from flask_jwt_extended import (jwt_required,
                                create_access_token,
                                create_refresh_token,
                                get_jwt_identity,
                                unset_jwt_cookies,
                                )

#register blue print
auth_bp = Blueprint('auth', __name__,url_prefix=AUTH_API_LINK)


@auth_bp.route('/login',methods=["POST"])
def login_user():
    req_body = request.get_json()
    try:
        user_email = req_body['user_email']
        user_password = req_body['user_password']
        check_exist=Users.query.filter_by(email=user_email).first()
        print("check email exist",check_exist)
        if check_exist is None:
            return make_response(jsonify({'status':'fail','msg':'email or password incorrect.'}),400)
        hash_password = check_exist.password
        # print("hash_password",hash_password)
        isPasswordCorrect = bcrypt.check_password_hash(hash_password,user_password)
        # print("passwordCorrect",isPasswordCorrect)
        if isPasswordCorrect:
            token_attributes={"id":check_exist.id,"name":check_exist.name,"email":check_exist.email}
            access_token = create_access_token(identity=token_attributes,fresh=True)
            refresh_token = create_refresh_token(identity=token_attributes)
            response={**token_attributes,"access_token": access_token,"refresh_token": refresh_token,"authenticated":True}
            return make_response(jsonify(response),201)
        else:
            return make_response(jsonify({'status':'fail','msg':'email or password incorrect.'}),400)
    except:
        return make_response(jsonify({"status":"failed","msg":"Internal Server Error"}),500)