from django.contrib import admin
from .models import NewUser
from django.contrib.auth.admin import UserAdmin
from rest_framework_simplejwt import token_blacklist

class OutstandingTokenAdmin(token_blacklist.admin.OutstandingTokenAdmin):

    def has_delete_permission(self, *args, **kwargs):
        return True # or whatever logic you want


admin.site.unregister(token_blacklist.models.OutstandingToken)
admin.site.register(token_blacklist.models.OutstandingToken, OutstandingTokenAdmin)

admin.site.site_header = "后台管理"
admin.site.site_title = '后台管理'

class UserAdminConfig(UserAdmin):
    model = NewUser
    search_fields = ('email', 'user_name')
    list_filter = ('email', 'user_name', 'is_useful', 'is_active', 'is_staff')
    ordering = ('-start_date',)
    list_display = ('email', 'id', 'user_name', 'is_useful', 'is_active', 'is_staff')
    fieldsets = (
        ('基础信息', {'fields': ('email', 'user_name', 'avatar')}),
        ('Permissions', {'fields': ('is_useful', 'is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'user_name', 'password1', 'password2', 'is_useful', 'is_active', 'is_staff')}
         ),
    )


admin.site.register(NewUser, UserAdminConfig)