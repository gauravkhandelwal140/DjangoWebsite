from django.shortcuts import render, redirect
from .models.product import Product
from .models.category import Category
from .models.customer import Customer
from django.views import View
from django.contrib.auth.hashers import make_password, check_password

# Create your views here.
def index(request):
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


class Signup(View):
    def get(self ,request):
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
                return redirect('homepage')
            else:
                error_message = 'You entered wrong password'

        else:
            error_message = 'Email does not exist'
        return render(request, 'store/login.html', {'error': error_message})
