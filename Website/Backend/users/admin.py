from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin

admin.site.site_title = '后台管理页面'
admin.site.site_header = "后台管理"

class UserAdminConfig(UserAdmin):
    model = User
    search_fields = ('email', 'user_name')
    list_filter = ('is_active', 'is_staff')
    ordering = ('-regtime',)
    list_display = ('email', 'id', 'user_name', 'musicID', 'musicEmail', 'is_active', 'is_staff', 'regtime')
    fieldsets = (
        ('基础信息', {'fields': ('email', 'user_name', 'avatar', 'musicID', 'musicEmail')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        ("添加新用户", {
            'classes': ('wide',),
            'fields': ('email', 'user_name', 'password1', 'password2', 'is_active', 'is_staff')}
        ),
    )

admin.site.register(User, UserAdminConfig)