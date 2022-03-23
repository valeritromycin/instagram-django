from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as UserAdminBase

from registration_app.models import Profile
from .models import Post


class ProfileInline(admin.StackedInline):
    model = Profile


admin.site.unregister(User)


@admin.register(User)
class UserAdmin(UserAdminBase):
    inlines = (
        ProfileInline,
    )


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'create_date', 'title',)
    ordering = ('id', '-create_date', )
    readonly_fields = ('create_date',)
    pass
