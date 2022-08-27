from django.urls import path
from .views import BlogViewSet, NewBlogViewSet, BlogDetailViewSet, BlogTypeViewSet, UserBlogViewSet, TypeBlogViewSet

urlpatterns = [
    # 注册路由
    path('', BlogViewSet.as_view(), name='blogs'),
    path('userBlogs/<int:userID>',
         UserBlogViewSet.as_view({'get': 'list'}), name='userBlogs'),
    path('typeBlogs/<int:typeID>',
         TypeBlogViewSet.as_view({'get': 'list'}), name='userBlogs'),

    path('detail/<int:pk>/',
         BlogDetailViewSet.as_view(), name="detail"),
    path('types/', BlogTypeViewSet.as_view(), name="types"),
    path('newBlog/', NewBlogViewSet.as_view(), name="newBlog"),
]
