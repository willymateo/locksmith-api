from django.contrib import admin

from .models import Password, PasswordCategory

admin.site.register(PasswordCategory)
admin.site.register(Password)
