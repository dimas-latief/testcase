from django.contrib import admin

# Register your models here.
from .models import Assets, Departments

admin.site.register(Assets)
admin.site.register(Departments)