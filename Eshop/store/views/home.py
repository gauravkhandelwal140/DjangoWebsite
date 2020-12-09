from django.shortcuts import render, redirect
from django.views import View

from ..models.product import Product
from ..models.category import Category


# Create your views here.
class Index(View):
    def get(self, request):
        cart=request.session.get('cart')
        if not cart:
            request.session.cart = {}
        data = {}
        products = None
        categories = Category.get_all_categories()
        categoryId = request.GET.get('category')
        if (categoryId):
            products = Product.get_products_by_category_id(categoryId)
        else:
            products = Product.get_all_products()

        data['products'] = products
        data['categories'] = categories
        return render(request, 'store/index.html', data)

    def post(self, request):
        remove=request.POST.get('remove')

        product_id = request.POST.get('product_id')
        cart = request.session.get('cart')
        if cart:
            quantity = cart.get(product_id)
            if quantity:
                if remove:
                    if quantity<=1:
                       cart.pop(product_id)
                    else:
                        cart[product_id] = quantity - 1
                else:
                    cart[product_id] = quantity + 1
            else:
                cart[product_id] = 1
        else:
            cart = {}
            cart[product_id] = 1
        request.session['cart'] = cart
        print('login', request.session.get('customer_email'))
        print('cart', request.session['cart'])
        return redirect('homepage')
