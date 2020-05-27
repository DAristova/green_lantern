from flask import Blueprint, render_template
from flask_login import current_user, login_required


orders = Blueprint('orders', __name__)


@orders.route('/orders')
@login_required
def list_of_orders():
    user = current_user
    result_dict = {}
    for order in user.orders:
        for line in order.order_lines:
            try:
                result_dict['price'] += line.good.price
            except KeyError:
                result_dict['price'] = line.good.price
    return render_template('orders.html', orders=user.orders, amount=result_dict['price'])
