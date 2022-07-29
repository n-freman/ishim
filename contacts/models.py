from django.db import models
from django.contrib.auth.models import User
from vacancy.models import Vacancy
from employee.models import CV


class Contact(models.Model):
    content = models.TextField()
    vacancy = models.OneToOneField(Vacancy, on_delete=models.CASCADE)

    def content_as_list(self):
        return self.content.split('\n')


class ChosenContact(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE)


class ChosenCVContact(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='cv_contacts',
    )
    cv = models.ForeignKey(
        CV,
        on_delete=models.CASCADE,
    )
    data = models.TextField()

    def content_as_list(self):
        return self.data.split('\n')