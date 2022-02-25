from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, CreateAPIView, DestroyAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

from .serializers import BlogSerializer, NewBlogSerializer, BlogDetailSerializer, BlogTypeSerializer, NewBlogTypeSerializer
from .models import Blog, BlogType

# 分页设置
class ArticlePagination(PageNumberPagination):
    page_size = 4

# 博客列表视图
class BlogViewSet(ListAPIView):
    serializer_class = BlogSerializer
    queryset = Blog.objects.all()
    pagination_class = ArticlePagination

# 创建博客视图
class NewBlogViewSet(CreateAPIView):
    permission_classes = [IsAuthenticated, ]
    serializer_class = NewBlogSerializer
    queryset = Blog.objects.all()

# 博客详情视图
class BlogDetailViewSet(RetrieveUpdateDestroyAPIView):
    serializer_class = BlogDetailSerializer
    queryset = Blog.objects.all()


# 博客标签列表视图
class BlogTypeViewSet(ListAPIView):
    serializer_class = BlogTypeSerializer
    queryset = BlogType.objects.all()

# 创建博客标签视图
class NewBlogTypeViewSet(CreateAPIView):
    # permission_classes = [IsAuthenticated, ]
    serializer_class = NewBlogTypeSerializer
    queryset = BlogType.objects.all()

