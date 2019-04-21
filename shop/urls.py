from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views
# from shop.views import ProductCreateView
from django.views.generic import TemplateView

app_name = 'shop'

urlpatterns = [
    url(r'^accounts/login/$', auth_views.login, name="login"),
    url(r'^logout/$', auth_views.logout, name="logout"),
    url(r'^password_change/$', auth_views.password_change, name="password_change_form"),
    url(r'^changepassword/done/$', auth_views.password_change_done, name="password_change_done"),
    url(r'^resetpassword/$', auth_views.password_reset, name="password_reset_form"),
    url(r'^resetpassword/confirm/$', auth_views.password_reset_confirm, name="password_reset_confirm"),
    url(r'^resetpassword/complete/$', auth_views.password_reset_complete, name="password_reset_complete"),
    url(r'^resetpassword/done/$', auth_views.password_reset_done, name="password_reset_done"),
    # url(r'^signup/$', views.UserSignUpView.as_view(), name='signup'),
    # url(
    #     r'^signup/success/$',
    #     TemplateView.as_view(template_name='registration/signup_success.html'),
    #     name="signup_success"
    # ),
    # url(
    #     r'^signup/already-logged-in/$',
    #     TemplateView.as_view(template_name='registration/already_logged_in.html'),
    #     name="already_logged_in"
    # ),
    # url(r'^create/$', ProductCreateView.as_view(), name='product_create'),
    url(r'^$', views.product_list, name='product_list'),
    url(r'^(?P<category_slug>[-\w]+)/$', views.product_list, name='product_list_by_category'),
    url(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$', views.product_detail, name='product_detail'),
    # url(r'^signup/$', views.create_user_view, name='signup'),
]
