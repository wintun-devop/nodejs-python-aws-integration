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
                                set_access_cookies,
                                set_refresh_cookies,
                                )
#error handling
from sqlalchemy import exc

#register blue print
auth_bp = Blueprint('auth', __name__,url_prefix=AUTH_API_LINK)


@auth_bp.route('/login',methods=["POST"])
def login_user():
    req_body = request.get_json()
    try:
        user_email = req_body['user_email']
        user_password = req_body['user_password']
        check_exist=Users.query.filter_by(email=user_email).first()
        # print("check email exist",check_exist)
        if check_exist is None:
            return make_response(jsonify({'status':'fail','msg':'email or password incorrect.'}),400)
        hash_password = check_exist.password
        # print("hash_password",hash_password)
        isPasswordCorrect = bcrypt.check_password_hash(hash_password,user_password)
        # print("passwordCorrect",isPasswordCorrect)
        if isPasswordCorrect:
            # create the jwt and go make response
            token_attributes={"id":check_exist.id,"name":check_exist.name,"email":check_exist.email}
            access_token = create_access_token(identity=token_attributes,fresh=True)
            refresh_token = create_refresh_token(identity=token_attributes)
            response=jsonify({**token_attributes,"access_token": access_token,"refresh_token": refresh_token,"authenticated":True})
            set_access_cookies(response, access_token)
            set_refresh_cookies(response,refresh_token)
            return make_response(response,201)
        else:
            return make_response(jsonify({'status':'fail','msg':'email or password incorrect.'}),400)
    except exc.SQLAlchemyError as e:
        # print(e)
        return make_response(jsonify({"status":"failed","msg":"Internal Server Error"}),500)


@auth_bp.route('/refresh', methods=['GET'])
@jwt_required(refresh=True)  #Require a valid refresh token for this route
def refresh():
    # Set the JWT access cookie in the response
    try:
        current_user = get_jwt_identity()
        # print("referse attribute",current_user)
        access_token = create_access_token(identity=current_user,fresh=False)
        refresh_token = create_refresh_token(identity=current_user)
        respone = jsonify({'refresh': True,'access_token':access_token,'refresh_token':refresh_token,**current_user})
        set_access_cookies(respone, access_token)
        set_refresh_cookies(respone,refresh_token)
        return make_response(respone, 200)
    except:
        return make_response(jsonify({"status":"Login expired!","msg":"Login Again!"}),400)


@auth_bp.route('/logout', methods=['DELETE'])
@jwt_required()  #Require a valid access token for this route
def logout():
    respone = jsonify({'logout': True})
    unset_jwt_cookies(respone)
    return respone, 200