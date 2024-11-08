from django.contrib import admin
from django.urls import path
from farmfreshapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.home, name='index'),
    path('products/', views.products, name='products'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
]
