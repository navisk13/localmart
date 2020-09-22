from django.conf.urls import url

from shop.views import ConfirmDelete
from . import views
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required

app_name = 'shop'

urlpatterns = [
    url(r'^accounts/login/$', auth_views.LoginView.as_view(), name="login"),
    url(r'^logout/$', auth_views.LogoutView.as_view(), name="logout"),
    url(r'^password_change/$', auth_views.PasswordChangeView.as_view(), name="password_change_form"),
    url(r'^changepassword/done/$', auth_views.PasswordChangeDoneView.as_view(), name="password_change_done"),
    url(r'^resetpassword/$', auth_views.PasswordResetView.as_view(), name="password_reset_form"),
    url(r'^resetpassword/confirm/$', auth_views.PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    url(r'^resetpassword/complete/$', auth_views.PasswordResetCompleteView.as_view(), name="password_reset_complete"),
    url(r'^resetpassword/done/$', auth_views.PasswordResetDoneView.as_view(), name="password_reset_done"),
    url(r'^signup/$',views.signup, name="signup"),
    url(r'^profile/$', views.profiledetailview, name="profile"),
    url(r'^profile/delete/$', ConfirmDelete.as_view(), name="profile_delete"),
    url(r'^profile/delete/confirm$', views.delete_profile, name="confirm_delete_profile"),
    url(r'^(?P<category_slug>[-\w]+)/$', views.product_list, name='product_list_by_category'),
    url(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$', views.product_detail, name='product_detail'),
    url(r'^$', views.product_list, name='product_list'),
    url(r'^profile/update/$', views.update_profile, name="profile_update"),

]
