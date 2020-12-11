from django.shortcuts import render, redirect
from ..models.product import Product
from django.views import View
from django.utils.decorators import method_decorator
from ..middleware.auth import auth_middleware
class Cart(View):
    @method_decorator(auth_middleware)
    def get(self, request):
        ids = list(request.session.get('cart').keys())
        product = Product.get_products_by_id(ids)
        print(product)
        return render(request, 'store/cart.html', {'products': product})



