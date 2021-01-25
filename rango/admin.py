from django.contrib import admin
# Register your models here.
from rango.models import Category, Page

class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'url')

# Add in this class to customise the Admin Interface
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name', )}

# Update the registration to include this customised interface
# we add these classes to the Django administration
admin.site.register(Category, CategoryAdmin)
admin.site.register(Page, PageAdmin)
