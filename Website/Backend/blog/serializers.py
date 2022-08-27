from rest_framework import serializers
from .models import Blog, BlogType
# 博客列表


class BlogSerializer(serializers.ModelSerializer):
    blog_type = serializers.StringRelatedField(many=True)
    authorName = serializers.SerializerMethodField()

    class Meta:
        model = Blog
        fields = ['id', 'blog_type', 'title',
                  'author', 'authorName', 'content']

    def get_authorName(self, object):
        return object.author.user_name
# 特定用户博客列表


class UserBlogSerializer(serializers.ModelSerializer):
    blog_type = serializers.StringRelatedField(many=True)
    authorName = serializers.SerializerMethodField()

    class Meta:
        model = Blog
        fields = ['id', 'blog_type', 'title',
                  'author', 'authorName', 'content']

    def get_authorName(self, object):
        return object.author.user_name
# 特定标签博客列表


class TypeBlogSerializer(serializers.ModelSerializer):
    blog_type = serializers.StringRelatedField(many=True)
    authorName = serializers.SerializerMethodField()

    class Meta:
        model = Blog
        fields = ['id', 'blog_type', 'title',
                  'author', 'authorName', 'content']

    def get_authorName(self, object):
        return object.author.user_name
# 博客详情


class BlogDetailSerializer(serializers.ModelSerializer):
    authorName = serializers.SerializerMethodField()

    class Meta:
        model = Blog
        fields = '__all__'

    def get_authorName(self, object):
        return object.author.user_name
# 博客标签列表


class BlogTypeSerializer(serializers.ModelSerializer):
    blog_count = serializers.SerializerMethodField()

    class Meta:
        model = BlogType
        fields = ['id', 'name', 'blog_count']

    def get_blog_count(self, object):
        return len([i for i in Blog.objects.filter(blog_type=object.id)])
# 创建博客


class NewBlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = '__all__'
