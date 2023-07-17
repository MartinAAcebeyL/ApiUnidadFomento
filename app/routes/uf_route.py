from app.controllers.uf_controllers import get_uf_value
from app.utils.responses import response, bad_request, not_found
from flask import Blueprint
from flasgger import swag_from

uf_api = Blueprint('uf_api', __name__, url_prefix='/api/v1/uf')


@uf_api.route('/<string:date>', methods=['GET'])
@swag_from('./documentation/uf/get_uf.yaml')
def get_uf(date: str):
    try:
        return response(get_uf_value(date), "UF value")
    except Exception as e:
        if e.args[0] == "Date out of range":
            return not_found(e.args[0])
        return bad_request(e.args[0])
    