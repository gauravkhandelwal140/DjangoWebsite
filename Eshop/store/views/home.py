from django.shortcuts import render, redirect
from django.views import View

from ..models.product import Product
from ..models.category import Category

# Create your views here.
class Index(View):
    def get(self,request):
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
        product_id=request.POST.get('product_id')
        print(product_id)
        return redirect('homepage')


