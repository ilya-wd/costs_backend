"""
Server
"""
from flask import Flask, request
import helpers

app = Flask(__name__)

basic_fee_distance = 2 * 100
cart_value_qualifies_small = 10 * 100
cart_value_qualifies_for_free = 100 * 100
cart_items_free_threshold = 4
cart_items_bulk_threshold = 12
max_delivery_fee = 15 * 100


@app.route('/json-example', methods=['POST'])
def json():
    request_data = request.get_json()

    cart_value = None
    delivery_distance = None
    number_of_items = None
    time = None
    delivery_fee = {'delivery_fee': 0}
    error_message = {'delivery_fee': "can't calculate. error in the request"}

    if request_data:
        if 'cart_value' in request_data:
            cart_value = request_data['cart_value']
        else:
            return error_message

        if 'delivery_distance' in request_data:
            delivery_distance = request_data['delivery_distance']
        else:
            return error_message

        if 'number_of_items' in request_data:
            number_of_items = request_data['number_of_items']
        else:
            return error_message

        if 'time' in request_data:
            time = request_data['time']
        else:
            return error_message

    if (helpers.delivery_is_free(cart_value_qualifies_for_free, cart_value)):
        return delivery_fee

    delivery_fee['delivery_fee'] += helpers.distance_fee(
        delivery_distance, basic_fee_distance)
    delivery_fee['delivery_fee'] += helpers.small_cart_fee(
        cart_value, cart_value_qualifies_small)
    delivery_fee['delivery_fee'] += helpers.items_fee(
        number_of_items, cart_items_bulk_threshold, cart_items_free_threshold)

    if helpers.rush_hour_fee(time):
        delivery_fee['delivery_fee'] *= 1.2
    delivery_fee['delivery_fee'] = helpers.delivery_fee_cap(
        delivery_fee['delivery_fee'], max_delivery_fee)

    return delivery_fee


if __name__ == '__main__':
    # run app in debug mode on port 5000
    app.run(debug=True, port=5000)
