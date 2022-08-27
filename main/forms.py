from django import forms
from phonenumber_field.formfields import PhoneNumberField


class PhoneNumEditForm(forms.Form):
    phone_num = PhoneNumberField()


class EmailEditForm(forms.Form):
    email = forms.EmailField()


class PasswordEditForm(forms.Form):
    password = forms.CharField(
        max_length=20)


class SphereEditForm(forms.Form):
    sphere = forms.CharField(max_length=65)


class CompNameEditForm(forms.Form):
    company_name = forms.CharField(max_length=65)


class CityEditForm(forms.Form):
    city = forms.CharField(max_length=65)


class LogoEditForm(forms.Form):
    logo = forms.ImageField()


class FirstNameEditForm(forms.Form):
    first_name = forms.CharField(max_length=65)


class LastNameEditForm(forms.Form):
    last_name = forms.CharField(max_length=65)