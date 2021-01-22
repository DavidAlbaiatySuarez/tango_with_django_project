from django.contrib import admin

# Register your models here.
from rango.models import Category, Page

# we add these classes to the Django administration
admin.site.register(Category)
admin.site.register(Page)
