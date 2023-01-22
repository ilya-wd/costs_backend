import math
import datetime


def small_cart_fee(cart_value, threshold_value):
    '''
    if cart value (eg 8 EUR) is smaller than threschold value ( eg 10 EUR as in requirements),
    the difference is added as a fee
    '''
    if cart_value < threshold_value:
        print('small cart fee applied:', threshold_value - cart_value)
        return threshold_value - cart_value
    return 0


def distance_fee(distance, basic_fee):
    '''
    a basic fee is applied to all deliveries, eg 2 EUR as in requirements
    then if the distance > 1000 (meters), 1 EUR is added for each 500m
    '''
    if distance < 1000:
        print('fee for distance is basic fee: ', basic_fee)
        return basic_fee
    print('fee for distance: ', basic_fee +
          math.ceil((distance - 1000) / 500) * 100)
    return basic_fee + math.ceil((distance - 1000) / 500) * 100


def delivery_is_free(cart_value_required, cart_value_customer):
    '''
    if cart's value is larger than specified value, eg 100 EUR as in requirements
    then delivery fee is 0
    using this method we can figure out if we need to do any calculations at all
    '''
    if cart_value_required <= cart_value_customer:
        print('free delivery!')
        return True
    return False


def items_fee(items, bulk_threshold_items, free_threshold_items):
    '''
    if a cart contains less than 4 items, then the fee is not increased
    for each items above 4, 50 cents are added to the fee
    if a cart has more than 12 items, a single bulk fee of 1 EUR 20 cents is applied
    '''
    added_fee = 0
    if items > bulk_threshold_items:
        added_fee += 1.20 * 100
    if items > free_threshold_items:
        added_fee += (items - free_threshold_items) * 50
    print('fee for number of items:', added_fee)
    return added_fee


def delivery_fee_cap(total_fee, cap):
    '''
    delivery fee can't be more than the cap, eg 15 EUR as in requirements
    '''
    if total_fee > cap:
        print('cap is reached:', cap)
        return cap
    print('cap is NOT reached:', total_fee)
    return total_fee


def rush_hour_fee(date_string):
    '''
    if the order is made betwen 15 and 19 on a Friday, an extra fee is applied
    '''
    date_format = "%Y-%m-%dT%H:%M:%SZ"
    date = datetime.datetime.strptime(date_string, date_format)

    if date.weekday() == 4 and 15 <= date.hour <= 19:
        print('rush hour fee applied:')
        return True
    print('not a rush hour:')
    return False
