from django.urls import path
from . import views

urlpatterns = [
    path('' , views.index , name = 'index'),
    path('password' , views.make_password , name = 'password'),
    path('about' , views.about, name = 'about'),
]
