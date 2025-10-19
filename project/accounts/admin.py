from django.contrib import admin

# Register your models here.
from accounts.models import User,Address


class AccountsAdmin(admin.ModelAdmin):
    list_display = ['fname','lname','username','email']
admin.site.register(User,AccountsAdmin)
admin.site.register(Address)