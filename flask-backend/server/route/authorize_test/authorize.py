from flask import Blueprint,jsonify,make_response,request
#import api prefix
from server.server_config import AUTH_API_LINK


#import token services
from flask_jwt_extended import (
                                jwt_required,
                                get_jwt
                                )

#register blue print
authorize_test_bp = Blueprint('authorize_test', __name__,url_prefix=AUTH_API_LINK)


@authorize_test_bp.route("/authorize",methods=['POST'])
@jwt_required()    #Require a valid access token for this route
def test_authorize_post():
    req_body = request.get_json()
    try:
        result = get_jwt()
        response ={**req_body,**result}
        return make_response(jsonify(response))
    except Exception as e:
        raise e
    
@authorize_test_bp.route("/authorize",methods=['GET'])
@jwt_required()    #Require a valid access token for this route
def test_authorize_get():
    try:
        result = get_jwt()
        response ={**result}
        return make_response(jsonify(response))
    except Exception as e:
        raise e
    