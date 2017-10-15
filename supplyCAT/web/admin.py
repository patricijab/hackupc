from django.contrib import admin

from .models import Category, MenuItem, Demand
admin.site.register(Category)
admin.site.register(MenuItem)
admin.site.register(Demand)

# Register your models here.
