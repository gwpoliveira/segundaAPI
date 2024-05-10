from django.contrib import admin
from .models import User, Profile, Todo


class AdminLogin(admin.ModelAdmin):
    list_display = ('username', 'email')


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'full_name', 'verified')

class TodoAdmin(admin.ModelAdmin):
    list_editable = ['completed']
    list_display = ['user', 'title', 'completed', 'date']


admin.site.register(User, AdminLogin)
admin.site.register(Profile, ProfileAdmin)
admin.site.register(Todo, TodoAdmin)

