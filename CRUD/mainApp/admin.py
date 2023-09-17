from django.contrib import admin
from .models import Employee


class Employee_Admin(admin.ModelAdmin):
    list_display = ("emp_id", "Name", "Department", "Salary")
    
    search_fields = ["Name"]

admin.site.register(Employee,Employee_Admin)

