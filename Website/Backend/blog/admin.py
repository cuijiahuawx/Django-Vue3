from django.contrib import admin
from .models import Blog, BlogType
# Register your models here.


@admin.register(BlogType)
class BlogTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'id', )


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'id', '_blog_type', 'author',
                    'created_time', 'last_update_time')

    def _blog_type(self, row):
        return ','.join([t.name for t in row.blog_type.all()])
