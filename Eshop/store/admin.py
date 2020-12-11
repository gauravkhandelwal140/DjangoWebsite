from django.contrib import admin

from .models.category import Category
from .models.customer import Customer
from .models.orders import Order
from .models.product import Product


# Register your models here.
class AdminProduct(admin.ModelAdmin):
    list_display = ['id', 'name', 'price', 'category']


class Admincategory(admin.ModelAdmin):
    list_display = ['id', 'name']


class Admincustomer(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'phone_no', 'email', 'password']


class Adminorder(admin.ModelAdmin):
    list_display = ['id', 'product', 'customer', 'quantity', 'price', 'address', 'phone', 'date', 'status']


admin.site.register(Product, AdminProduct)
admin.site.register(Category, Admincategory)
admin.site.register(Customer, Admincustomer)
admin.site.register(Order, Adminorder)
