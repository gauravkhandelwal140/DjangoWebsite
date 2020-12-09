from django.shortcuts import render, redirect
from ..models.customer import Customer
from django.views import View
from django.contrib.auth.hashers import make_password



class Signup(View):
    def get(self ,request):
        print(request.session.get('customer_email'))
        return render(request, 'store/signup.html', )

    def post(self, request):
        first_name = request.POST.get('firstname')
        last_name = request.POST.get('lastname')
        email = request.POST.get('email')
        phone_no = request.POST.get('phone')
        password = request.POST.get('password')
        print(first_name, last_name, phone_no, email, password)
        # validation
        value = {
            'first_name': first_name,
            'last_name': last_name,
            'email': email,
            'phone_no': phone_no
        }
        error_message = None
        customer = Customer(first_name=first_name,
                            last_name=last_name,
                            email=email,
                            phone_no=phone_no,
                            password=password)

        if len(phone_no) < 10:
            error_message = "Phone number must be 10 characters long"
        elif len(password) < 6:
            error_message = "Password must be at least 6 characters long"
        elif customer.isExists():
            error_message = "Customer Already Exists"

        # saving
        if not error_message:
            customer.password = make_password(customer.password)
            customer.register()
            return redirect('homepage')
        else:
            data = {'error': error_message, 'values': value}
            return render(request, 'store/signup.html', data)
