from django.shortcuts import render, get_object_or_404
from .models import Category, Product
from cart.forms import CartAddProductForm
# from django.contrib.auth import views as auth_views
from django.shortcuts import redirect, render
# from django.urls import reverse_lazy
# from django.views.generic import CreateView, UpdateView, DetailView, ListView, View
# from shop.models import UserInfo
# from shop.forms import UserSignUpForm
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.db import transaction

# from shop.forms import SignUpForm,ProfileForm



# class UserSignUpView(CreateView):
#     form_class = UserSignUpForm
#     template_name = 'registration/signup.html'
#     success_url = reverse_lazy('signup_success')
#
#     def get(self, request, *args, **kwargs):
#         if request.user.is_authenticated:
#             return redirect('already_logged_in')
#         return super(UserSignUpView, self).get(request, *args, **kwargs)


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


# def login(request,  *args, **kwargs):  # view to handle remember me and login
#     if request.method == 'POST':
#         if not request.POST.get('remember_me'):
#             request.session.set_expiry(0)
#         else:
#             request.session.set_expiry(1000)
#     if request.method == 'GET' and request.user.is_authenticated:
#         return redirect('already_logged_in')
#     return auth_views.login(request, *args, **kwargs)

# class ProductCreateView(CreateView):
#     model = Product
#     fields = ['category', 'name', 'image', 'description', 'price', 'available', 'stock']
#
#     def form_valid(self, form):
#         form.instance.created_by = self.request.user
#         response = super(ProductCreateView, self).form_valid(form)
#         return response

# @transaction.atomic
# def create_user_view(request):
#     if request.method == 'POST':
#         user_form = SignUpForm(request.POST)
#         profile_form = ProfileForm(request.POST)
#         if user_form.is_valid() and profile_form.is_valid():
#             user = user_form.save()
#             user.refresh_from_db()  # This will load the Profile created by the Signal
#             profile_form = ProfileForm(request.POST, instance=user.profile)  # Reload the profile form with the profile instance
#             profile_form.full_clean()  # Manually clean the form this time. It is implicitly called by "is_valid()" method
#             profile_form.save()  # Gracefully save the form
#     else:
#         user_form = SignUpForm()
#         profile_form = ProfileForm()
#     return render(request, 'shop/signup.html', {
#         'user_form': user_form,
#         'profile_form': profile_form
# })