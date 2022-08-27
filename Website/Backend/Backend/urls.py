from django.contrib import admin
from django.urls import path, include
# 引入SimpleJWT相关库
from Utils.simpleJwt import MyTokenObtainPairView
from rest_framework_simplejwt.views import (
    TokenRefreshView,
    TokenVerifyView,
)


urlpatterns = [
    # 管理页面路由
    path('admin/', admin.site.urls),
    # SimpleJWT相关路由
    path('api/token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    # 自定义App的路由
    path('blog/', include('blog.urls'), name='blog'),
    path('user/', include('users.urls'), name='user'),

]
