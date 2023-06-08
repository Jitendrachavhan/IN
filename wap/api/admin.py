from django.contrib import admin

# Register your models here.

from .models import User, Pet

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'password']
    



@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description', 'content', 'date', 'user']    
