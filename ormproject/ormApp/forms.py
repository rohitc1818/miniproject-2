from django import forms
from ormApp.models import Employee

# create your form view here.
class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = "__all__"

