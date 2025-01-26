from django.contrib import admin
from .models import Department, Position, Employee

# Admin model for Department
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)
    ordering = ('name',)

# Admin model for Position
class PositionAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')
    search_fields = ('title',)
    ordering = ('title',)

# Admin model for Employee
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'position', 'department', 'salary', 'date_of_hire')
    search_fields = ('first_name', 'last_name', 'email')
    list_filter = ('department', 'position', 'gender', 'date_of_hire')
    ordering = ('last_name', 'first_name')
    date_hierarchy = 'date_of_hire'

    # Remove filter_horizontal as it's not needed for ForeignKey relationships
    # filter_horizontal = ('position',)  # This line is removed

# Register the models and their admin configurations
admin.site.register(Department, DepartmentAdmin)
admin.site.register(Position, PositionAdmin)
admin.site.register(Employee, EmployeeAdmin)
