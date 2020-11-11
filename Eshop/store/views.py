from django.http import HttpResponse
from django.shortcuts import render
from .models.product import Product
from .models.category import Category
from .models.costomer import Costomer


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


def signup(request):
    if request.method == 'GET':
        return render(request, 'store/signup.html')
    else:
        first_name = request.POST.get('firstname')
        last_name = request.POST.get('lastname')
        email = request.POST.get('email')
        phone_no = request.POST.get('phone')
        password = request.POST.get('password')
        print(first_name, last_name, phone_no, email, password)

        customer=Costomer(first_name=first_name,
                           last_name=last_name,
                           email=email,
                           phone_no=phone_no,
                           password=password)
        customer.register()
        return render(request, 'store/signup.html')