from django.contrib import admin
from .models import BlogType, Blog


@admin.register(BlogType)
class BlogTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'id', )

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'id', '_blog_type', 'author', 'created_time', 'last_updated_time')

    def _blog_type(self, row):
        return ','.join([x.name for x in row.blog_type.all()])
