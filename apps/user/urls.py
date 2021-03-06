
from django.contrib import admin
from django.urls import path
from django.urls import path,include,re_path
from user.views import RegisterView, ActiveView, LoginView, UserOrderView, UserInfoView, UserAddressView, \
   LogoutView,UserChangeAddress, UserImage,ChangePassword, SendCode,ImageCode
from django.conf.urls import  url
from django.contrib.auth.decorators import login_required

app_name = 'user'
urlpatterns = [
   url(r"^register/$", RegisterView.as_view(), name='register'),
   url(r"^login/$", LoginView.as_view(), name="login"),
   url(r"^active/(?P<token>.*)/$", ActiveView.as_view()),
   url(r"^$", UserInfoView.as_view(), name='user'),# 用户中心信息页
   url(r"^order/(?P<page>\d+)/$", UserOrderView.as_view(), name='order'),
   url(r"^address/$", UserAddressView.as_view(), name='address'),
   url(r"^logout/$", LogoutView.as_view(), name='logout'),# 注销登录
   url(r'^change_address/$', UserChangeAddress.as_view(), name='change_address'),# 修改地址
   url(r'^change_image/$', UserImage.as_view(), name='change_image'),# 修改头像
   url(r'^change_password/$', ChangePassword.as_view(), name='ChangePassword'),# 修改密码
   url(r'^send_code/$', SendCode.as_view(), name='SendCode'),# 修改密码
   url(r'^ImageCode/$', ImageCode.as_view(), name='ImageCode'),# 验证码图片

]