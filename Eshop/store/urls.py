from django.urls import path
from .views import index
from .views import signup


urlpatterns = [
    path('', index),
    path('signup/', signup)

]
