from django import forms
from .models import *


class CompanyCreateForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ['company_name', 'sphere', 'phone_num', 'city']


class EnterpreneuerCreateForm(forms.ModelForm):
    class Meta:
        model = Enterpreneuer
        fields = ['company_name', 'sphere', 'phone_num', 'city', 'logo']
    
