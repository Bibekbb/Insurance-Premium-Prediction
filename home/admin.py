from django.contrib import admin
from home.models import UserCreateForm
# Register your models her

@admin.register(UserCreateForm)
class UserADmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'password', 'confirm_password']
