from django.http import JsonResponse
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import viewsets
from .serializers import BlogSerializer, UserBlogSerializer, TypeBlogSerializer, BlogTypeSerializer, NewBlogSerializer, BlogDetailSerializer
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from .models import Blog, BlogType
# 分页设置


class ArticlePagination(PageNumberPagination):
    page_size = 2   # default page size
    page_size_query_param = 'size'  # ?page=xx&size=??
    max_page_size = 30  # max page size
# 博客列表视图


class BlogViewSet(ListAPIView):
    serializer_class = BlogSerializer
    queryset = Blog.objects.all()
    pagination_class = ArticlePagination
# 特定用户博客列表视图


class UserBlogViewSet(viewsets.ModelViewSet):
    serializer_class = UserBlogSerializer
    pagination_class = ArticlePagination

    def get_queryset(self):
        userID = self.kwargs['userID']

        queryset = Blog.objects.filter(author__id=userID)

        return queryset


class TypeBlogViewSet(viewsets.ModelViewSet):
    serializer_class = TypeBlogSerializer
    pagination_class = ArticlePagination

    def get_queryset(self):
        typeID = self.kwargs['typeID']

        queryset = Blog.objects.filter(blog_type__id__contains=typeID)

        return queryset
# 博客详情视图
# 查询、修改、删除一个


class BlogDetailViewSet(RetrieveUpdateDestroyAPIView):
    serializer_class = BlogDetailSerializer
    queryset = Blog.objects.all()
# 博客标签列表视图


class BlogTypeViewSet(ListAPIView):
    serializer_class = BlogTypeSerializer
    queryset = BlogType.objects.all()
# 创建博客视图


class NewBlogViewSet(CreateAPIView):
    # permission_classes = [IsAuthenticated, ]
    serializer_class = NewBlogSerializer
    queryset = Blog.objects.all()
