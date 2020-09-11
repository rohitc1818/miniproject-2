from django.contrib import admin
from ormApp.models import Employee

# Register your models here.
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['name','age','salary','address']

admin.site.register(Employee,EmployeeAdmin)

# username: ss
# password: ss123
# email: ss@gmail.com