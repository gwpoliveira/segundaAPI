from django.contrib import admin
from .models import User, Profile


class AdminLogin(admin.ModelAdmin):
    list_display = ('username', 'email')


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'full_name', 'verified')


admin.site.register(User, AdminLogin)
admin.site.register(Profile, ProfileAdmin)
