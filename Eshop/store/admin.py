from django.contrib import admin
from .models.product import Product
from .models.category import Category
from .models.customer import Customer

# Register your models here.
class AdminProduct(admin.ModelAdmin):
    list_display = ['name', 'price', 'category']


class Admincategory(admin.ModelAdmin):
    list_display = ['name']

class Admincustomer(admin.ModelAdmin):
    list_display = ['first_name', 'last_name','phone_no','email','password']

admin.site.register(Product, AdminProduct)
admin.site.register(Category, Admincategory)
admin.site.register(Customer,Admincustomer)
