import sys

from flask import jsonify, request, abort, Blueprint, make_response
from application import discount_db, serial_number_db
from application.discount_service import DiscountService
from utils.custom_exceptions import NoMoreDiscountException

discount_service = DiscountService(discount_db, serial_number_db)
views = Blueprint('views', __name__, url_prefix='/')


@views.route('/discount', methods=['GET'])
def get():
    try:
        serial_number = request.args.get('serial_number')
        if not serial_number:
            abort(400, {"message": "Please enter a serial number"})
        if not discount_service.exists(serial_number):
            abort(404, {"message": "The serial number %s is unknown" % serial_number})
        discount = discount_service.get_discount(serial_number)
        if not discount:
            discount = discount_service.set_discount(serial_number)
        return jsonify({'discount': discount})
    except NoMoreDiscountException:
        abort(410)


@views.errorhandler(400)
def bad_request(error):
    return make_response(jsonify({'error': error.description['message']}), 400)


@views.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': error.description['message']}), 404)


@views.errorhandler(410)
def no_more_discount():
    return make_response(jsonify({'error': 'No more discounts available for the moment'}), 410)


@views.errorhandler(500)
def server_error(error):
    sys.stderr.write("Request path: %s Request method: %s with error %s\n" %
                     (request.path, request.method, str(error)))
    return make_response(jsonify({'error': 'Internal error :('}), 500)
