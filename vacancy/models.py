from django.db import models
from django.contrib.auth.models import User
from rest_framework import serializers


class Vacancy(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    position = models.CharField(max_length=65)
    sphere = models.CharField(max_length=100)
    min_salary = models.IntegerField(default=0)
    max_salary = models.IntegerField()
    registration = models.CharField(max_length=100, default='не имеет значения')
    experience = models.CharField(max_length=65)
    min_age = models.IntegerField()
    max_age = models.IntegerField()
    sex = models.CharField(max_length=65, default='не имеет значения')
    education = models.CharField(max_length=65)
    responsibilities = models.TextField()
    work_terms = models.TextField()
    busyness = models.CharField(max_length=65, default='')
    work_graph = models.CharField(max_length=65)
    payment = models.TextField(default='')
    views = models.IntegerField(default=0)
    creation_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.creator.email} {self.position}'
    
    class Meta:
        verbose_name_plural = "Vacancies"


class NeededLanguage(models.Model):
    vacancy = models.ForeignKey(Vacancy, on_delete=models.CASCADE)
    language = models.CharField(max_length=25)
    level = models.CharField(max_length=65)


class VacancySerializer(serializers.ModelSerializer):
    class Meta:
        model = Vacancy
        fields = '__all__'
