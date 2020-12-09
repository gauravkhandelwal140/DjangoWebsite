from django.urls import path
from .views import home, login, signup
from .views.signup import Signup
from .views.login import Login,logout
from .views.cart import Cart


from .views.home import Index

urlpatterns = [
    path('', Index.as_view(), name='homepage'),
    path('signup/', Signup.as_view(),name='signup' ),
    path('login/', Login.as_view(),name='login'),
    path('logout/',logout,name='logout'),
    path('cart/',Cart.as_view(),name='cart'),
]
