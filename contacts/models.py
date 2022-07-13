from django.db import models
from django.contrib.auth.models import User
from vacancy.models import Vacancy


class Contact(models.Model):
    content = models.TextField()
    vacancy = models.OneToOneField(Vacancy, on_delete=models.CASCADE)

    def content_as_list(self):
        return self.content.split('\n')


class ChosenContact(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE)