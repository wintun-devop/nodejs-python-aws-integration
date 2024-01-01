from flask import Blueprint,jsonify,make_response

test_bp = Blueprint('test', __name__)

@test_bp.route('/',methods=["GET"])
def index():
    response = {
        "status":"success",
        "message":"API Server is working well!"
    }
    return make_response(jsonify(response))
    