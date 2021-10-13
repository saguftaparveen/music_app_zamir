from os import name
from post.forms import Registerform
from django.urls import path

from . import views

urlpatterns = [
    path('premium/',views.premium,name='premium'),
    path('',views.my_index,name='my_index'),
    # path('forms/',views.manualform,name='manualform'),
    # path('',views.index,name='index'),
    path('home/', views.index, name='index'),
    path('signup/', views.signup, name="signup"),
    path('loginform/',views.manualform, name="loginform"),
    path('registerform/',views.registerview,name="registerform"),
    path('logout/',views.logoutview,name="logout")
]