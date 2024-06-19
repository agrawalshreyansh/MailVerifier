from django.contrib import admin
from .models import *

class Registered_Users(admin.ModelAdmin):
    pass


admin.site.register( User_Login_Data, Registered_Users)