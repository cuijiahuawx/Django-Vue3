from django.urls import path
from .views import BlogViewSet, NewBlogViewSet, BlogDetailViewSet, BlogTypeViewSet, NewBlogTypeViewSet

urlpatterns = [
    # 博客列表
    path('', BlogViewSet.as_view(), name="blogs"),
    path('newBlog/', NewBlogViewSet.as_view(), name="newBlog"),
    path('detail/<int:pk>/', BlogDetailViewSet.as_view(), name="detail"),
    path('types/', BlogTypeViewSet.as_view(), name="types"),
    path('newType/', NewBlogTypeViewSet.as_view(), name="newType"),
]