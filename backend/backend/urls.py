from django.contrib import admin
from django.urls import path, include
# 引入SimpleJWT相关库
from Utils.simpleJwt import MyTokenObtainPairView
from rest_framework_simplejwt.views import (
    TokenRefreshView,
    TokenVerifyView,
)
# 设置网站图标
from django.views.generic.base import RedirectView
from django.conf.urls import url

from .views import home


urlpatterns = [
    url(r'^favicon\.ico/pre>', RedirectView.as_view(url=r'static/favicon.ico')),
    path('admin/', admin.site.urls),
    # SimpleJWT相关路由
    path('api/token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    # 自定义App的路由
    path('', home, name='home'),
    path('user/', include('user.urls'), name='user'),
    path('blogs/', include('blog.urls'), name='blog'),
]



