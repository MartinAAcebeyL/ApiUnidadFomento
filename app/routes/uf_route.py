from app.controllers.uf_controllers import get_uf_value
from . import Blueprint, jsonify

uf_api = Blueprint('uf_api', __name__, url_prefix='/api/v1/uf')

@uf_api.route('/<string:date>', methods=['GET'])
def get_uf(date: str):
    try:
        return get_uf_value(date)
    except Exception as e:
        return jsonify({'error': str(e)}), 500