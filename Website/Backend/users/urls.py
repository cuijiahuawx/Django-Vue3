from django.urls import path
from .views import EditProfileViewSet, RegisterViewSet, send_code

urlpatterns = [
    # 注册路由
    path('register/', RegisterViewSet.as_view(), name='register'),
    # 更改用户信息路由
    path('edit_profile/', EditProfileViewSet.as_view(), name='edit_profile'),
    # 验证码路由
    path('send_code/', send_code, name='send_code'),
]

