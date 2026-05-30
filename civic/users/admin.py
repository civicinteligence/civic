from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import OfficeUser

class OfficeUserAdmin(UserAdmin):
    model = OfficeUser
    fieldsets = UserAdmin.fieldsets + (
        ('Civic Profile Info', {'fields': ('office_name', 'issue_category')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Civic Profile Info', {'fields': ('office_name', 'issue_category')}),
    )

admin.site.register(OfficeUser, OfficeUserAdmin)