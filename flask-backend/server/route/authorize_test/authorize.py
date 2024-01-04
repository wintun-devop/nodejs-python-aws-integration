from flask import Blueprint,jsonify,make_response,request
#import api prefix
from server.server_config import AUTH_API_LINK


#import token services
from flask_jwt_extended import (
                                jwt_required,
                                get_jwt_identity,
                                unset_jwt_cookies
                                )