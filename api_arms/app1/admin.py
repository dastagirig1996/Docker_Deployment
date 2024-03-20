from django.contrib import admin
from .models import MyUser  # Import your MyUser model here

# Define the admin class for MyUser
class MyUserAdmin(admin.ModelAdmin):
    search_fields = ['username', 'email'] 
    # You can customize the admin options here if needed

# Register MyUser with the admin site
admin.site.register(MyUser, MyUserAdmin)

