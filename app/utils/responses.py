from flask import jsonify


def response(data: dict, message: str):
    return jsonify(
        {
            'succses': True,
            'message': message,
            'data': data
        }
    ), 200


def not_found(message):
    return jsonify(
        {
            'succses': False,
            'data': {},
            'message': message,
            'code': 404
        }
    ), 404


def bad_request(message):
    return jsonify(
        {
            'succses': False,
            'data': {},
            'message': message,
            'code': 400
        }
    ), 400


def token_time_out():
    return jsonify(
        {
            'succses': False,
            'data': {},
            'message': "El token expiro",
            'code': 400
        }
    ), 400


def token_error():
    return jsonify(
        {
            'succses': False,
            'data': {},
            'message': "Error en la validacion del token",
            'code': 400
        }
    ), 400
