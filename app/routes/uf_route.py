from app.controllers.uf_controllers import get_uf_value
from . import Blueprint
from app.utils.responses import response, bad_request, not_found


uf_api = Blueprint('uf_api', __name__, url_prefix='/api/v1/uf')


@uf_api.route('/<string:date>', methods=['GET'])
def get_uf(date: str):
    try:
        return response(get_uf_value(date), "UF value")
    except Exception as e:
        if e.args[0] == "Date out of range":
            return not_found(e.args[0])
        return bad_request(e.args[0])
