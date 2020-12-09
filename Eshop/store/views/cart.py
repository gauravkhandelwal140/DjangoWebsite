from django.shortcuts import render, redirect
from ..models.product import Product
from django.views import View



class Cart(View):

    def get(self, request):
        ids=list(request.session.get('cart').keys())
        product=Product.get_products_by_id(ids)
        print(product)
        return render(request, 'store/cart.html',{ 'product':product })

    # def post(self, request):
    #     error_message = None
    #     email = request.POST.get('email')
    #     password = request.POST.get('password')
    #     customer = Customer.get_customer_by_email(email)
    #     if customer:
    #         flag = check_password(password, customer.password)
    #         if flag:
    #             request.session['customer']=customer.id
    #             request.session['customer_email']=customer.email
    #             request.session['customer_name']=customer.first_name
    #
    #             return redirect('homepage')
    #         else:
    #             error_message = 'You entered wrong password'
    #
    #     else:
    #         error_message = 'Email does not exist'
    #     return render(request, 'store/login.html', {'error': error_message})
