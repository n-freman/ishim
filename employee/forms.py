from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import *


class UserCreateForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['email', 'password1', 'password2']


class EmployeeCreateForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['first_name', 'last_name', 'city', 'phone_num', 'sex']


class CVCreationForm(forms.ModelForm):
    class Meta:
        model = CV
        fields = [
            'first_name', 
            'last_name', 
            'mobile_num', 
            'email', 
            'registration', 
            'sex', 
            'position', 
            'sphere', 
            'min_salary',
            'busyness',
            'work_graph',
            'about'
            ]


class WorkExpCreateForm(forms.ModelForm):
    class Meta:
        model = WorkExperience
        fields =[
            'position',
            'org_name',
            'responsibilities',
            'start_year',
            'end_year'
        ]


class EduCreateForm(forms.ModelForm):
    class Meta:
        model = Education
        fields = [
            'degree',
            'establishment',
            'faculty',
            'specialization',
            'start_year',
            'end_year',
        ]


