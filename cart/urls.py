from django.conf.urls import url
from . import views
from django.contrib.auth.decorators import login_required


app_name = 'cart'

urlpatterns = [
    url(r'^$', login_required(views.cart_detail), name='cart_detail'),
    url(r'^add/(?P<product_id>\d+)/$', views.cart_add, name='cart_add'),
    url(r'^remove/(?P<product_id>\d+)/$', views.cart_remove, name='cart_remove'),
]

