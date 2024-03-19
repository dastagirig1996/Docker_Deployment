from django.contrib import admin

# Register your models here.
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

# Import your MyUser model
from .models import MyUser

# Define admin class for MyUser
class MyUserAdmin(admin.ModelAdmin):
    pass  # You can customize the admin options here

# Register MyUser model with the admin site
admin.site.register(MyUser, MyUserAdmin)

# Register TokenAdmin with MyUser
TokenAdmin.autocomplete_fields = ['user']

