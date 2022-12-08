from django.shortcuts import render
from . forms import UserForm
from django.http import HttpResponseRedirect


def index(request):
    return render(request, 'website/index.html', {})


def shop(request):
    return render(request, 'website/shop.html', {})


def about(request):
    return render(request, 'website/about.html', {})


def shop_details(request):
    return render(request, 'website/shop-details.html', {})


def add_to_cart(request):
    return render(request, 'website/shopping-cart.html', {})


def checkout(request):
    return render(request, 'website/checkout.html', {})


def blog_details(request):
    return render(request, 'website/blog-details.html', {})


def blog(request):
    return render(request, 'website/blog.html', {})


def contact(request):
    return render(request, 'website/contact.html', {})

# User login and logout


