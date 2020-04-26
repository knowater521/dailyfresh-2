
from django.contrib import admin
from django.urls import path
from django.urls import path,include,re_path
from user.views import RegisterView, ActiveView, LoginView, UserOrderView, UserInfoView, UserAddressView
from django.conf.urls import  url

app_name = 'user'
urlpatterns = [
   url(r"^register/$", RegisterView.as_view(), name='register'),
   url(r"^login/$", LoginView.as_view(), name="login"),
   url(r"^active/(?P<token>.*)/$", ActiveView.as_view()),
   url(r"^$", UserOrderView.as_view(), name='order'),# 用户中心信息页
   url(r"^order/$", UserInfoView.as_view(), name='user'),
   url(r"^address/$", UserAddressView.as_view(), name='address'),

]