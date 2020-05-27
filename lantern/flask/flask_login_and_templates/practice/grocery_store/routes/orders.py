from flask import Blueprint, render_template
from flask_login import current_user, login_required


orders = Blueprint('orders', __name__)


@orders.route('/orders')
@login_required
def list_of_orders():
    user = current_user
    price_sum = 0
    for order in user.orders:
        for line in order.order_lines:
            price_sum += line.good.price
    return render_template('orders.html', orders=user.orders, amount=price_sum)
