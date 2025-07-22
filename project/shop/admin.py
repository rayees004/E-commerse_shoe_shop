from django.contrib import admin
from .models import *
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}
admin.site.register(Category,CategoryAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name','slug','price','img','stock','available']
    list_editable = ['price','img','stock','available']
    prepopulated_fields = {'slug':('name',)}
admin.site.register(Product,ProductAdmin)

