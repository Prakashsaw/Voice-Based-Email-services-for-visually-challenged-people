from django.contrib import admin
from django.contrib.admin.sites import site
from homepage.models import UserDetails, option


# Register your models here.

class UserDetailsAdmin(admin.ModelAdmin):
    list_display=('email','password')

class optionAdmin(admin.ModelAdmin):
    list_display=('option',)

admin.site.register(UserDetails,UserDetailsAdmin)

admin.site.register(option,optionAdmin)
