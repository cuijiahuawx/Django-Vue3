from rest_framework import serializers
from .models import Blog, BlogType

# 博客列表
class BlogSerializer(serializers.ModelSerializer):
    blog_type = serializers.StringRelatedField(many=True)

    class Meta:
        model = Blog
        fields = ['id', 'blog_type', 'title', 'content']

# 创建博客
class NewBlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = '__all__'

# 博客详情
class BlogDetailSerializer(serializers.ModelSerializer):
    blog_type = serializers.StringRelatedField(many=True)
    author = serializers.StringRelatedField()

    class Meta:
        model = Blog
        fields = '__all__'

# 博客标签列表
class BlogTypeSerializer(serializers.ModelSerializer):
    blog_count = serializers.SerializerMethodField()

    class Meta:
        model = BlogType
        fields = ['id', 'name', 'blog_count']

    def get_blog_count(self, object):
        return len([i for i in Blog.objects.filter(blog_type=object.id)])

# 创建博客标签
class NewBlogTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogType
        fields = '__all__'
