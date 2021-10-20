from django.contrib import admin
from application.models import Employee

# Register your models here.

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['id', 'firstname', 'lastname', 'image', 'email', 'salary', 'created_date', 'updated_date']

    class Meta:
        model = Employee

admin.site.register(Employee, EmployeeAdmin)