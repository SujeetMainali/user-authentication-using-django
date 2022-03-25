from unicodedata import name
from . import views
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index, name='index'),
    path('login', views.userlogin, name='login'),
    path('logout', views.userlogout, name='logout')
]