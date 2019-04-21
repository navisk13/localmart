from django.conf.urls import url
from . import views
from django.contrib.auth.decorators import login_required


app_name = 'orders'

urlpatterns = [
    url(r'^create/$', login_required(views.order_create), name='order_create')
]