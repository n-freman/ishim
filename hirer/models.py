from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
import os


class Hirer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    company_name = models.CharField(max_length=65)
    sphere = models.CharField(max_length=100)
    phone_num = PhoneNumberField()
    city = models.CharField(max_length=65)
    creation_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.company_name


class Company(Hirer):
    pass

class Enterpreneuer(Hirer):
    logo = models.ImageField(default='default.jpg', upload_to='logos')

    def delete(self, *args, **kwargs):
        self.logo.delete()
        super(Image, self).delete(*args, **kwargs)

