from django.http import HttpResponse
from django.shortcuts import render, redirect
from ..models.customer import Customer
from django.views import View
from django.contrib.auth.hashers import check_password


class Login(View):

    def get(self, request):
        return render(request, 'store/login.html')

    def post(self, request):
        error_message = None
        email = request.POST.get('email')
        password = request.POST.get('password')
        customer = Customer.get_customer_by_email(email)
        if customer:
            flag = check_password(password, customer.password)
            if flag:
                request.session['customer_id']=customer.id
                request.session['customer_email']=customer.email

                return redirect('homepage')
            else:
                error_message = 'You entered wrong password'

        else:
            error_message = 'Email does not exist'
        return render(request, 'store/login.html', {'error': error_message})
