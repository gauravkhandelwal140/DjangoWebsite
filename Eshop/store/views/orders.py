from django.shortcuts import render, redirect

from django.contrib.auth.hashers import check_password
from ..models.customer import Customer
from django.views import View

from ..models.product import Product
from ..models.orders import Order

from ..middleware.auth import auth_middleware
from django.utils.decorators import method_decorator


class OrderView(View):
    @method_decorator(auth_middleware)
    def get(self, request):
        customer = request.session.get('customer')
        orders = Order.get_orders_by_customer(customer)
        print(orders)
        orders=orders.reverse()
        return render(request, 'store/orders.html', {'orders': orders})
