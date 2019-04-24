from django.conf.urls import url
from django.shortcuts import render, get_object_or_404
from .models import Category, Product
from cart.forms import CartAddProductForm
# from django.contrib.auth import views as auth_views
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DetailView, ListView, View
from shop.models import Profile
from shop.forms import SignUpForm
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.db import transaction
from django.contrib.auth.models import User
from django.shortcuts import HttpResponseRedirect, reverse
from django.views.generic import TemplateView

from shop.forms import SignUpForm, UpdateProfile


def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=category)

    context = {
        'category': category,
        'categories': categories,
        'products': products
    }
    return render(request, 'shop/product/list.html', context)


def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    cart_product_form = CartAddProductForm()
    context = {
        'product': product,
        'cart_product_form': cart_product_form
    }
    return render(request, 'shop/product/detail.html', context)


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            user.profile.address = form.cleaned_data.get('address')
            user.profile.phone = form.cleaned_data.get('phone')
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('/')
    else:
        if request.user.is_authenticated:
            return redirect('/')
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})


def profiledetailview(request):
    if request.user.is_authenticated:
        profile = Profile.objects.get(user=request.user)
        context = {'profile': profile}
        return render(request, 'registration/profile.html', context)
    else:
        return redirect('login')


def update_profile(request):
    instance = Profile.objects.get(user=request.user)
    args = {}
    if request.method == 'POST':
        form = UpdateProfile(request.POST, instance=instance)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            firstn = form.cleaned_data['first_name']
            lastn = form.cleaned_data['last_name']
            user = request.user
            user.username = username
            user.email = email
            user.first_name = firstn
            user.last_name = lastn
            user.save()
            form.save()
            return HttpResponseRedirect("/profile")
    else:
        form = UpdateProfile()

    args['form'] = form
    return render(request, 'registration/update_profile.html', args)


def delete_profile(request):
    user = request.user
    profile = Profile.objects.get(user=user)
    profile.delete()
    user.delete()
    return redirect('/')


class ConfirmDelete(View):
    def get(self, request, *args, **kwargs):
        return render(request,'registration/confirm_delete.html')

