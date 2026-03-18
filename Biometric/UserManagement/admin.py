from django.contrib import admin

from .models import Item, UserAttendance, UserRegistraion

admin.site.register(UserRegistraion)
admin.site.register(Item)
admin.site.register(UserAttendance)
