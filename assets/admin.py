from django.contrib import admin

# Register your models here.
from .models import Assets, Departments, Employee

admin.site.register(Assets)
admin.site.register(Departments)
admin.site.register(Employee)