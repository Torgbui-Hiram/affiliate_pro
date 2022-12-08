from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('shop', views.shop, name='shop'),
    path('about', views.about, name='about'),
    path('shop-details', views.shop_details, name='details'),
    path('shoping-cart', views.add_to_cart, name='shopping-cart'),
    path('checkout', views.checkout, name='checkout'),
    path('blog-details', views.blog_details, name='blog-details'),
    path('blog', views.blog, name='blog'),
    path('contact', views.contact, name='contact'),
]
