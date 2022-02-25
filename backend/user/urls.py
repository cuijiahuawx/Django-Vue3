from django.urls import path
from .views import RegisterViewSet, VerifyEmailViewSet, EditProfileViewSet, ForgetPasswordViewSet, ChangePasswordViewSet, ChangeEmailViewSet
# edit_profile
urlpatterns = [
    # 注册路由
    path('', RegisterViewSet.as_view(), name='register'),
    # 用户激活邮箱路由
    path('verify_email/', VerifyEmailViewSet.as_view(), name='verify_email'),
    # 更改用户信息路由
    # path('edit_profile/', edit_profile, name='edit_profile'),
    path('edit_profile/', EditProfileViewSet.as_view(), name='edit_profile'),
    # 更改密码路由
    path('forget/', ForgetPasswordViewSet.as_view(), name='forget'),
    path('change_password/', ChangePasswordViewSet.as_view(), name='change_password'),
    # 更改邮箱路由
    path('change_email/', ChangeEmailViewSet.as_view(), name='change_email'),

]

