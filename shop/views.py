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

from shop.forms import SignUpForm,ProfileForm


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


# class UserSignUpView(CreateView):
#     form_class = SignUpForm
#     template_name = 'registration/signup.html'
#     success_url = reverse_lazy('login')
#
#     def get(self, request, *args, **kwargs):
#         if request.user.is_authenticated:
#             return redirect('home')
#         return super(UserSignUpView, self).get(request, *args, **kwargs)
#     def post(self, request, *args, **kwargs):
#         username = self.request.POST['username']
#         password = self.request.POST['password1']
#         user = User.objects.only(username=username)
#         login(self.request, user)
#         return super(UserSignUpView, self).post(request,*args, **kwargs)

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})

class UserUpdateView(UpdateView):
    model = Profile
    form_class = ProfileForm
    template_name = 'registration/signup.html'

    def form_valid(self, form):
        response = super(UserUpdateView, self).form_valid(form)
        if form.is_valid():
            user = form.instance.user
            user.first_name = form.cleaned_data['first_name']
            user.last_name = form.cleaned_data['last_name']
            user.email = form.cleaned_data['email']
            user.save()
        return response

    def get_context_data(self, **kwargs):
        context = super(UserUpdateView, self).get_context_data(**kwargs)
        user = context['form'].instance.user
        context['form'].fields['first_name'].initial = user.first_name
        context['form'].fields['last_name'].initial = user.last_name
        context['form'].fields['email'].initial = user.email
        context['heading'] = 'Update profile'
        return context

    def get(self, request, *args, **kwargs):
        if request.user != self.get_object().user:
            return redirect('permission_denied')
        return super(UserUpdateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        if request.user != self.get_object().user:
            return redirect('permission_denied')
        return super(UserUpdateView, self).post(request, *args, **kwargs)


class ProfileDetailView(DetailView):
    model = User
    template_name = 'registration/profile.html'

    def get_context_data(self, **kwargs):
        context = super(ProfileDetailView, self).get_context_data(**kwargs)
        try:
            context['user_info'] = Profile.objects.get(user=self.get_object())
        except User.DoesNotExist:
            context['error'] = 'No data found for this user!'
        return context

