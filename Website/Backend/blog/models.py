from django.db import models
from users.models import User


class BlogType(models.Model):
    name = models.CharField(
        max_length=15,
        verbose_name='文章标签'
    )

    class Meta:
        verbose_name = '博客分类'
        verbose_name_plural = verbose_name

    def __str__(self):
        return f'{self.name}'


class Blog(models.Model):
    title = models.CharField(
        max_length=50,
        verbose_name='文章标题'
    )
    blog_type = models.ManyToManyField(
        BlogType,
        verbose_name='文章标签',
        related_name='blog',
        related_query_name='blog'
    )
    content = models.TextField(
        max_length=10000,
        verbose_name='文章内容'
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='author',
        related_query_name='author',
        verbose_name='作者'
    )
    created_time = models.DateTimeField(
        auto_now_add=True,
        verbose_name='创建时间'
    )
    last_update_time = models.DateTimeField(
        auto_now=True,
        verbose_name='编辑时间'
    )

    class Meta:
        ordering = ['-created_time']
        verbose_name = '博客'
        verbose_name_plural = verbose_name

    def __str__(self):
        return f"{self.title}"
